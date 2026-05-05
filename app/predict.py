import os
import uuid
import cv2
import numpy as np
import random
from PIL import Image
try:
    import tensorflow as tf
    TF_AVAILABLE = True
except (ImportError, MemoryError):
    TF_AVAILABLE = False
from config import Config
from app.disease_meta import DISEASE_META

# ── Load model once at import time 
_model = None

def get_model():
    global _model
    if not TF_AVAILABLE:
        return None
    if _model is None:
        # Support both .h5 (legacy) and .keras (Keras 3) formats
        model_path = Config.MODEL_PATH
        keras_path = str(model_path).replace('.h5', '.keras')
        if os.path.exists(keras_path):
            _model = tf.keras.models.load_model(keras_path)
        elif os.path.exists(model_path):
            _model = tf.keras.models.load_model(model_path)
    return _model


# ── Disease metadata — imported from disease_meta.py ────
# Remedies and descriptions are written in plain, simple language
# so any farmer or student can understand what to do.
# To edit disease info, open: app/disease_meta.py


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def save_upload(file) -> str:
    """Save uploaded file with unique name. Returns filename."""
    ext = file.filename.rsplit('.', 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    save_path = os.path.join(Config.UPLOAD_FOLDER, unique_name)
    file.save(save_path)
    return unique_name


def _isolate_leaf(img_bgr: np.ndarray) -> np.ndarray:
    """
    Segments the main leaf from the image background using HSV color masking
    and places it on a dark background — exactly like PlantVillage training images.

    Why this matters:
      The model was trained on PlantVillage, where every image is a SINGLE isolated
      leaf on a BLACK background. Google images have complex backgrounds (grass, sky,
      multiple leaves, etc.). By isolating just the leaf, we make Google images
      look similar to training data, so the model can actually recognise them.
    """
    h, w = img_bgr.shape[:2]
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # ── Build colour mask for leaf-like pixels 
    # Covers: green, yellow-green, yellow, light brown, dark brown, red-brown
    masks = [
        cv2.inRange(img_hsv, np.array([22, 25, 25]),  np.array([100, 255, 255])),  # green/yellow
        cv2.inRange(img_hsv, np.array([5,  25, 25]),  np.array([22,  255, 220])),  # brown/orange
        cv2.inRange(img_hsv, np.array([150,25, 25]),  np.array([179, 255, 255])),  # dark red-brown
    ]
    leaf_mask = masks[0]
    for m in masks[1:]:
        leaf_mask = cv2.bitwise_or(leaf_mask, m)

    # ── Morphological cleanup — fill holes, remove noise 
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    kernel_open  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel_close)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN,  kernel_open)

    # ── Keep only the largest contiguous leaf region ─────
    contours, _ = cv2.findContours(leaf_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        area_ratio = cv2.contourArea(largest) / (h * w)
        if area_ratio > 0.04:  # leaf covers at least 4% of image
            clean_mask = np.zeros_like(leaf_mask)
            cv2.drawContours(clean_mask, [largest], -1, 255, cv2.FILLED)
            # Small dilation to soften leaf edges
            edge_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            clean_mask  = cv2.dilate(clean_mask, edge_kernel, iterations=2)
            leaf_mask   = clean_mask

    # ── If isolation failed (mask too empty), fall back to original ───────────
    leaf_pixel_ratio = np.sum(leaf_mask > 0) / (h * w)
    if leaf_pixel_ratio < 0.04:
        return img_bgr  # fallback: use the original image

    # ── Apply mask: keep leaf pixels, set background to dark (8, 8, 8) ───────
    result = img_bgr.copy()
    result[leaf_mask == 0] = [8, 8, 8]  # near-black, matching PlantVillage bg
    return result


def _apply_temperature_scaling(probs: np.ndarray, temperature: float = 3.0) -> np.ndarray:
    """
    Apply temperature scaling to calibrate the model's overconfident softmax outputs.

    The raw model outputs 99.9% for most inputs because EfficientNet trained on
    PlantVillage is extremely confident within its training distribution.
    Temperature scaling (T > 1) softens the distribution to give realistic scores.

    T = 1.0  → no change (raw model output)
    T = 2.0  → moderately softer (realistic for good images)
    T = 3.0  → softer still  (realistic for Google/internet images)
    T = 5.0  → very soft     (use for very uncertain inputs)

    Reference: "On Calibration of Modern Neural Networks" — Guo et al., ICML 2017
    """
    log_probs = np.log(np.clip(probs, 1e-9, 1.0))
    scaled    = log_probs / temperature
    scaled   -= np.max(scaled)   # numerical stability
    exp_p     = np.exp(scaled)
    return exp_p / np.sum(exp_p)


def preprocess_image(image_path: str) -> np.ndarray:
    """
    Full preprocessing pipeline:
      1. Load image
      2. Isolate the leaf (remove complex backgrounds)
      3. Resize to model input size (224×224)
      4. Convert to float32 — EfficientNet expects [0, 255]
    """
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        raise ValueError(f"Cannot read image: {image_path}")

    # Isolate leaf from background (makes Google images work like PlantVillage)
    img_bgr = _isolate_leaf(img_bgr)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, Config.IMG_SIZE)
    img_rgb = img_rgb.astype(np.float32)
    img_rgb = np.expand_dims(img_rgb, axis=0)  # shape: (1, 224, 224, 3)
    return img_rgb


def _basic_leaf_check(image_path: str) -> tuple[bool, str]:
    """
    Minimal sanity check — just confirms there are leaf-like colours present.
    We no longer block Google images; this only rejects completely invalid inputs
    (non-plant objects: hands, walls, cars, etc.).
    """
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return False, "Could not read the image file."

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    total   = img_bgr.shape[0] * img_bgr.shape[1]

    # Any green/yellow/brown content at all?
    green  = cv2.inRange(img_hsv, np.array([22, 25, 25]), np.array([100, 255, 255]))
    yellow = cv2.inRange(img_hsv, np.array([15, 25, 25]), np.array([22,  255, 255]))
    brown  = cv2.inRange(img_hsv, np.array([5,  25, 25]), np.array([22,  220, 200]))

    leaf_ratio = (cv2.countNonZero(green) + cv2.countNonZero(yellow) + cv2.countNonZero(brown)) / total

    if leaf_ratio < 0.08:
        return False, (
            f"No plant leaf detected in this image (only {leaf_ratio*100:.1f}% leaf-like colours). "
            "Please upload an image of a plant leaf."
        )
    return True, "OK"


# ── Main Prediction Function ───────

def predict_disease(image_path: str) -> dict:
    """
    Full prediction pipeline with leaf isolation and confidence calibration.
    """
    try:
        model = get_model()
        if model is None:
            return _demo_prediction()

        # ── STEP 1: Quick sanity check (rejects non-plant images) ────────────────
        is_leaf, reason = _basic_leaf_check(image_path)
        if not is_leaf:
            return {
                'class_name':     'Unknown',
                'plant_type':     'Unknown',
                'disease_name':   'No Leaf Detected',
                'confidence':     0.0,
                'confidence_pct': 0.0,
                'is_healthy':     False,
                'severity':       'Unknown',
                'remedy':         reason,
                'description':    'Please upload a clear image of a plant leaf to get a disease diagnosis.',
                'top3':           [],
            }

        # ── STEP 2 & 3: Preprocess (with leaf isolation) + Inference ─────────────
        img   = preprocess_image(image_path)
        preds = model.predict(img, verbose=0)   # shape: (1, 38), raw softmax

        # ── STEP 4: Temperature scaling — calibrate overconfident outputs ─────────
        raw_probs    = preds[0]
        scaled_probs = _apply_temperature_scaling(raw_probs, temperature=3.0)

        top_idx    = int(np.argmax(scaled_probs))
        confidence = float(scaled_probs[top_idx])
        class_name = Config.CLASS_NAMES[top_idx]

        # Top-3 with calibrated confidences
        top3_idx = np.argsort(scaled_probs)[::-1][:3]
        top3 = [
            {'class': Config.CLASS_NAMES[i], 'confidence': round(float(scaled_probs[i]) * 100, 2)}
            for i in top3_idx
        ]

        # ── STEP 5: Low confidence → model is genuinely uncertain ────────────────
        if confidence < 0.40:
            return {
                'class_name':     'Uncertain',
                'plant_type':     'Unknown',
                'disease_name':   'Low Confidence Detection',
                'confidence':     confidence,
                'confidence_pct': round(confidence * 100, 2),
                'is_healthy':     False,
                'severity':       'Unknown',
                'remedy':         (
                    f"The model's best guess is '{class_name.replace('___', ' - ').replace('_', ' ')}' "
                    f"but with only {confidence*100:.1f}% confidence after calibration. "
                    "Try uploading a clearer, close-up photo of just the leaf for better accuracy."
                ),
                'description':    (
                    "This plant species may not be in the supported list, or the image quality "
                    "is too low for reliable detection. Supported plants: Apple, Cherry, Corn, Grape, "
                    "Orange, Peach, Pepper, Potato, Strawberry, Tomato, and more."
                ),
                'top3': top3,
            }

        # ── STEP 6: Return confident prediction ──────────────────────────────────
        meta = DISEASE_META.get(class_name, {
            'plant':    'Unknown',
            'disease':  class_name.replace('___', ' - ').replace('_', ' '),
            'severity': 'Medium',
            'healthy':  False,
            'remedy':   'Consult an agronomist.',
            'description': 'No detailed information available for this class.'
        })

        return {
            'class_name':     class_name,
            'plant_type':     meta['plant'],
            'disease_name':   meta['disease'],
            'confidence':     confidence,
            'confidence_pct': round(confidence * 100, 2),
            'is_healthy':     meta['healthy'],
            'severity':       meta['severity'],
            'remedy':         meta['remedy'],
            'description':    meta['description'],
            'simple_summary': meta.get('simple_summary', 'Follow the step-by-step guide below to treat your plant.'),
            'urgency_label':  meta.get('urgency_label', 'Act soon' if meta['severity'] != 'Healthy' else ''),
            'what_to_buy':    meta.get('what_to_buy', []),
            'top3':           top3,
        }
    except Exception as e:
        return {
            'class_name':     'Error',
            'plant_type':     'System Error',
            'disease_name':   'Server Exception',
            'confidence':     0.0,
            'confidence_pct': 0.0,
            'is_healthy':     False,
            'severity':       'High',
            'remedy':         'An error occurred on the server while analyzing the image.',
            'description':    f"Error Details: {str(e)}",
            'simple_summary': 'An error occurred during AI inference.',
            'urgency_label':  'Error',
            'what_to_buy':    [],
            'top3':           [],
        }


def _demo_prediction() -> dict:
    """Fallback when model is not yet trained — returns demo result."""
    return {
        'class_name':     'Tomato___Late_blight',
        'plant_type':     'Tomato',
        'disease_name':   'Late Blight (Demo Mode)',
        'confidence':     0.9423,
        'confidence_pct': 94.23,
        'is_healthy':     False,
        'severity':       'High',
        'remedy':         '1. Pull out and destroy all severely infected plants immediately.\n2. Do NOT put them in the compost.\n3. Buy an anti-fungal spray from your nearest agri-store.\n4. Spray the remaining plants today.\n5. Stop watering from above — water only at the roots.',
        'description':    'Demo mode active — train the CNN model first using the Jupyter Notebook.',
        'simple_summary': 'Your plant has caught a very fast-spreading sickness. The brown patches will kill the plant in days if you don\'t act right now.',
        'urgency_label':  'Today! Very Urgent',
        'what_to_buy':    ['Late Blight Fungicide Spray (ask for Mancozeb)', 'Hand gloves for safe removal'],
        'top3': [
            {'class': 'Tomato___Late_blight',  'confidence': 94.23},
            {'class': 'Tomato___Early_blight', 'confidence': 3.11},
            {'class': 'Tomato___healthy',      'confidence': 1.42},
        ],
    }


