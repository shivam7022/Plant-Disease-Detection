=======================================================
PLANT DISEASE DETECTION MODEL - USAGE INSTRUCTIONS
=======================================================

This folder contains the trained AI model for detecting plant diseases from leaf images. 
If you are integrating this model into a new project, please follow these instructions carefully.

---
1. FILES INCLUDED
---
1. plant_disease_model.keras : The trained neural network model.
2. class_names.json          : The exact list of 38 plant diseases the model can detect.

---
2. TECHNICAL REQUIREMENTS
---
To use this model without errors, your project must meet these conditions:

* Target Image Size : 224 x 224 pixels (Mandatory: The model will fail if the image is a different size).
* Color Format      : RGB
* Dependencies      : TensorFlow >= 2.15.0, NumPy, Pillow.

---
3. HOW TO USE IN PYTHON
---
Install requirements:
pip install tensorflow numpy pillow

Example Code snippet:

import numpy as np
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# 1. Load Model & Class Names
print("Loading model...")
model = load_model('plant_disease_model.keras')

with open('class_names.json', 'r') as f:
    CLASS_NAMES = json.load(f)

# 2. Process Image (Must be 224x224)
img_path = 'your_test_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Note: If your model requires normalization (e.g., /255.0), do it here:
# img_array = img_array / 255.0

# 3. Predict
predictions = model.predict(img_array)
predicted_index = np.argmax(predictions[0])
confidence = float(np.max(predictions[0])) * 100

print(f"Prediction: {CLASS_NAMES[predicted_index]}")
print(f"Confidence: {confidence:.2f}%")

=======================================================
Troubleshooting:
- If predictions are random, ensure you are resizing to exactly 224x224.
- If you get a "Custom object not found" error, update your TensorFlow version.
- Make sure you are using the provided class_names.json so the output index maps to the correct disease.
