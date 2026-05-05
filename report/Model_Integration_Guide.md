# Plant Disease Detection Model - Integration Guide

This document provides a comprehensive guide on how to integrate the trained `plant_disease_model.keras` into any new project. It covers the necessary components, a step-by-step code implementation in Python, explanations, and common potential issues you might face.

---

## 1. Prerequisites: What You Need
To successfully use the AI model in a new project, you must carry over **three critical components** from the original project:

1. **The Model File:** `plant_disease_model.keras` (The brain of the system).
2. **The Class Labels:** A list or JSON file (`class_names.json`) containing the exact 38 plant disease names in the exact order.
3. **Image Configuration:** The knowledge of the input dimensions. The model expects images to be exactly **224x224 pixels**.

---

## 2. Step-by-Step Python Integration

If your new project is built in Python (e.g., a Django app, FastAPI backend, or a standalone script), here is how you can use the model.

### Step 2.1: Install Dependencies
Your new environment must have TensorFlow/Keras installed.
```bash
pip install tensorflow numpy pillow
```

### Step 2.2: The Code Implementation
Create a python script (e.g., `predictor.py`) and use the following code:

```python
import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PlantDiseasePredictor:
    def __init__(self, model_path, labels_path):
        """
        Initializes the model and loads the class names.
        """
        print("Loading model... Please wait.")
        self.model = load_model(model_path)
        
        # Load class names from a JSON file (or define them as a list directly)
        with open(labels_path, 'r') as f:
            self.class_names = json.load(f)
            
        self.target_size = (224, 224) # Must match the training size
        print("Model loaded successfully!")

    def predict_image(self, img_path):
        """
        Processes an image and returns the predicted disease name.
        """
        # 1. Load the image and resize it to 224x224
        img = image.load_img(img_path, target_size=self.target_size)
        
        # 2. Convert the image to a NumPy array
        img_array = image.img_to_array(img)
        
        # 3. Expand dimensions to create a batch of 1 (Shape becomes: [1, 224, 224, 3])
        img_array = np.expand_dims(img_array, axis=0)
        
        # NOTE: If your model was trained with pixel normalization (e.g., dividing by 255), 
        # uncomment the line below. (EfficientNet often handles its own normalization, 
        # but standard CNNs usually require this).
        # img_array = img_array / 255.0

        # 4. Make the prediction
        predictions = self.model.predict(img_array)
        
        # 5. Get the index of the highest probability
        predicted_class_index = np.argmax(predictions[0])
        confidence_score = float(np.max(predictions[0])) * 100
        
        # 6. Map the index to the disease name
        predicted_disease = self.class_names[predicted_class_index]
        
        return {
            "disease": predicted_disease,
            "confidence": f"{confidence_score:.2f}%"
        }

# --- Usage Example ---
if __name__ == "__main__":
    predictor = PlantDiseasePredictor(
        model_path='plant_disease_model.keras', 
        labels_path='class_names.json'
    )
    
    result = predictor.predict_image('sample_leaf.jpg')
    print(f"Result: {result['disease']} (Confidence: {result['confidence']})")
```

---

## 3. Using in Non-Python Projects (Node.js, Mobile, Web)

If your new project is **NOT** in Python (for example, a React web app, an Android app, or a Node.js server), you cannot run the `.keras` file directly. You have two options:

### Option A: The API Approach (Recommended)
Keep the model wrapped in a small Python server (like Flask or FastAPI) and create an API endpoint (e.g., `/predict`). 
Your Node.js or Mobile app will send the image to this API via a POST request, and the Python server will return the JSON result.

### Option B: Model Conversion
- **For Web (JavaScript):** Convert the `.keras` file to **TensorFlow.js** format using the `tensorflowjs_converter`.
- **For Mobile (Android/iOS):** Convert the model to **TensorFlow Lite (.tflite)** format for on-device inference.

---

## 4. Potential Issues & Troubleshooting

When moving a machine learning model to a new project, developers often face these common pitfalls:

### ⚠️ Issue 1: Image Preprocessing Mismatch
**Problem:** The new project predicts random or wrong diseases with very low confidence, even though the model is 100% accurate.
**Cause:** The image wasn't processed exactly the way it was during training.
**Solution:** 
- Ensure the image size is strictly `224x224`. 
- Check if the original project divided pixel arrays by `255.0` (normalization). If it did, your new project must do the same. If it used a specific preprocessing function like `tf.keras.applications.efficientnet.preprocess_input`, you must import and use that exact function.

### ⚠️ Issue 2: TensorFlow Version Incompatibility
**Problem:** Error like `ValueError: Unable to restore custom object` or the `.keras` file simply fails to load.
**Cause:** The new project has a vastly different version of TensorFlow than the one used to train the model.
**Solution:** Check the original project's `requirements.txt`. Install the exact same or a compatible `tensorflow` version in your new project (e.g., `pip install tensorflow==2.15.0`).

### ⚠️ Issue 3: Missing or Mismatched Class Labels
**Problem:** The model predicts "index 15" but you don't know what disease that is, or the disease names are swapped.
**Cause:** You forgot to copy the `class_names.json` file, or the array order in the new project is different.
**Solution:** Machine learning models rely heavily on the **exact index order**. Always copy the labels directly from the source project. Do not sort them alphabetically again in the new project if they are already mapped.

### ⚠️ Issue 4: High Memory Usage (Server Crashing)
**Problem:** If you deploy this in a web app, the server RAM fills up quickly, and the app crashes.
**Cause:** Loading a Deep Learning model consumes a lot of RAM (500MB to 1GB+). If you load the model *inside* the route function, it will load a new copy into RAM for every single user request.
**Solution:** **Always load the model globally** (outside of the API route function) when the server starts, as shown in the `PlantDiseasePredictor` class example above. Use `self.model.predict()` inside the request handler.
