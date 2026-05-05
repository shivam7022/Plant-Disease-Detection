import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # ── Flask ───────
    SECRET_KEY = os.environ.get('SECRET_KEY', 'plant-disease-secret-key-2024')
    DEBUG = True

    # ── Upload ──────
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

    # ── Database ─────
    # Using SQLite for simplicity (no MySQL server required)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "plant_diseases.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ── Model ───────
    MODEL_PATH       = os.path.join(BASE_DIR, 'model', 'plant_disease_model.h5')
    MODEL_PATH_KERAS = os.path.join(BASE_DIR, 'model', 'plant_disease_model.keras')
    MODEL_PATH_TFLITE = os.path.join(BASE_DIR, 'model', 'plant_disease_model.tflite')
    IMG_SIZE         = (224, 224)

    # ── Disease Classes (38 PlantVillage classes, alphabetical) ─
    CLASS_NAMES = [
        'Apple___Apple_scab',
        'Apple___Black_rot',
        'Apple___Cedar_apple_rust',
        'Apple___healthy',
        'Blueberry___healthy',
        'Cherry_(including_sour)___Powdery_mildew',
        'Cherry_(including_sour)___healthy',
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
        'Corn_(maize)___Common_rust_',
        'Corn_(maize)___Northern_Leaf_Blight',
        'Corn_(maize)___healthy',
        'Grape___Black_rot',
        'Grape___Esca_(Black_Measles)',
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
        'Grape___healthy',
        'Orange___Haunglongbing_(Citrus_greening)',
        'Peach___Bacterial_spot',
        'Peach___healthy',
        'Pepper,_bell___Bacterial_spot',
        'Pepper,_bell___healthy',
        'Potato___Early_blight',
        'Potato___Late_blight',
        'Potato___healthy',
        'Raspberry___healthy',
        'Soybean___healthy',
        'Squash___Powdery_mildew',
        'Strawberry___Leaf_scorch',
        'Strawberry___healthy',
        'Tomato___Bacterial_spot',
        'Tomato___Early_blight',
        'Tomato___Late_blight',
        'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot',
        'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot',
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'Tomato___Tomato_mosaic_virus',
        'Tomato___healthy',
    ]
