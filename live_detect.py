import cv2
import numpy as np
import os
import sys

# Try to import TensorFlow
try:
    import tensorflow as tf
except ImportError:
    print("Error: TensorFlow is not installed. Please install it using 'pip install tensorflow'.")
    sys.exit(1)

# Import our Config class from the project
from config import Config

def main():
    print("Loading AI model... Please wait.")
    
    # Support both .keras and .h5 paths
    model_path = Config.MODEL_PATH_KERAS
    if not os.path.exists(model_path):
        model_path = Config.MODEL_PATH
    
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}.")
        print("Make sure you have trained and saved the model first.")
        sys.exit(1)
        
    # Load the Keras model
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
    
    # Open the webcam (0 is usually the default built-in laptop webcam)
    print("Opening webcam... Hold a leaf in front of the camera.")
    print("Press 'q' on your keyboard to quit the application.")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit(1)
        
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
            
        # ── 1. PREPROCESS THE FRAME ──────────────────────────────
        # The model expects a 224x224 RGB image
        img = cv2.resize(frame, Config.IMG_SIZE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32)
        img = np.expand_dims(img, axis=0) # Add batch dimension: (1, 224, 224, 3)
        
        # ── 2. PREDICT ───────────────────────────────────────────
        preds = model.predict(img, verbose=0)
        top_idx = int(np.argmax(preds[0]))
        confidence = float(preds[0][top_idx])
        class_name = Config.CLASS_NAMES[top_idx]
        
        # Format the text nicely
        display_name = class_name.replace('___', ' - ').replace('_', ' ')
        text = f"{display_name}: {confidence*100:.1f}%"
        
        # ── 3. DRAW RESULTS ON SCREEN ────────────────────────────
        # Pick green color if healthy, red if diseased
        if 'healthy' in class_name.lower():
            text_color = (0, 255, 0) # BGR: Green
        else:
            text_color = (0, 0, 255) # BGR: Red
            
        # Draw a semi-transparent black background box so text is readable
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        box_coords = ((10, 10), (20 + text_width, 20 + text_height + 10))
        cv2.rectangle(frame, box_coords[0], box_coords[1], (0, 0, 0), cv2.FILLED)
        
        # Draw the text overlay
        cv2.putText(frame, text, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)
        
        # Display the live video feed
        cv2.imshow('Live Plant Disease Detection', frame)
        
        # Check if the user pressed the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
