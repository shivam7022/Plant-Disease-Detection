# 🍃 LeafCare AI - Plant Disease Detection

An intelligent, full-stack web application designed to help farmers and gardeners diagnose plant diseases instantly. Simply upload a photo of a plant leaf, and the AI will detect the disease, assess the severity, and provide actionable, step-by-step remedies.

**Live Demo:** [https://plant-disease-detection-qebh.onrender.com/](https://plant-disease-detection-qebh.onrender.com/)

---

## ✨ Features

- **Accurate AI Diagnosis:** Powered by a fine-tuned EfficientNetB0 CNN model trained on the PlantVillage dataset (detects 38+ plant/disease classes).
- **Extremely Fast Inference:** Model is converted to **TensorFlow Lite (TFLite)** to allow high-speed, low-memory inference directly on standard web servers.
- **Actionable Advice:** Returns plain-language severity warnings, simple step-by-step remedies, and a shopping list for treatments.
- **Interactive UI:** A beautiful, responsive frontend with drag-and-drop upload, micro-animations, and dynamic progress bars.
- **Prediction History:** Tracks past predictions using a lightweight SQLite database, complete with filtering and pagination.
- **Leaf Isolation Processing:** Uses OpenCV to isolate leaves from complex backgrounds (like grass or hands) prior to AI inference, improving accuracy on real-world images.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3 (Vanilla, custom UI/UX), JavaScript
- **Backend:** Python 3.11, Flask, SQLAlchemy (SQLite)
- **Machine Learning:** TensorFlow Lite, OpenCV, NumPy
- **Deployment:** Render (Gunicorn)

---

## 🚀 Local Setup & Installation

Follow these steps to run the application on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/shivam7022/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python run.py
```

*The app will be available at `http://localhost:5000`.*

---

## ☁️ Deployment (Render)

This application is highly optimized for deployment on free-tier platforms like **Render**.

1. The AI model has been converted to `plant_disease_model.tflite` to bypass strict memory limits (512MB RAM).
2. The `tflite-runtime` package is used in production instead of the heavy `tensorflow` library.
3. The server starts via Gunicorn using the command: `gunicorn run:app`

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
