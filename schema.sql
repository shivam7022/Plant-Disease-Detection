-- ============================================================
-- Plant Disease Detection System — MySQL Schema
-- ============================================================

CREATE DATABASE IF NOT EXISTS plant_diseases_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE plant_diseases_db;

-- -----------------------------------------------
-- Table: predictions
-- Stores each image upload and its CNN result
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS predictions (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    image_filename   VARCHAR(255)      NOT NULL,
    plant_type       VARCHAR(100)      NOT NULL,
    disease_name     VARCHAR(255)      NOT NULL,
    confidence       FLOAT             NOT NULL,
    is_healthy       TINYINT(1)        DEFAULT 0,
    remedy           TEXT,
    description      TEXT,
    severity         ENUM('Low','Medium','High','Healthy') DEFAULT 'Medium',
    uploaded_at      DATETIME          DEFAULT CURRENT_TIMESTAMP,
    ip_address       VARCHAR(45)
);

-- -----------------------------------------------
-- Table: disease_info
-- Static lookup table: disease metadata & remedies
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS disease_info (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    class_name       VARCHAR(255)      UNIQUE NOT NULL,
    plant_type       VARCHAR(100)      NOT NULL,
    disease_name     VARCHAR(255)      NOT NULL,
    description      TEXT,
    symptoms         TEXT,
    remedy           TEXT,
    severity         ENUM('Low','Medium','High','Healthy') DEFAULT 'Medium',
    is_healthy       TINYINT(1)        DEFAULT 0
);

-- -----------------------------------------------
-- Sample disease info seed data
-- -----------------------------------------------
INSERT INTO disease_info (class_name, plant_type, disease_name, description, symptoms, remedy, severity, is_healthy) VALUES
('Tomato_healthy',           'Tomato',  'Healthy',             'No disease detected.',           'Leaves appear green and vigorous.',    'No treatment needed. Maintain proper watering and nutrition.', 'Healthy', 1),
('Tomato_Early_blight',      'Tomato',  'Early Blight',        'Caused by Alternaria solani.',   'Dark concentric rings on lower leaves.','Apply copper-based fungicide. Remove infected leaves.',        'Medium',  0),
('Tomato_Late_blight',       'Tomato',  'Late Blight',         'Caused by Phytophthora infestans.','Water-soaked brown lesions.',         'Use Mancozeb or Metalaxyl fungicides immediately.',            'High',    0),
('Tomato_Leaf_Mold',         'Tomato',  'Leaf Mold',           'Caused by Passalora fulva.',     'Yellow spots on upper leaf surface.',  'Improve ventilation, apply fungicides like chlorothalonil.',   'Medium',  0),
('Tomato_Septoria_leaf_spot','Tomato',  'Septoria Leaf Spot',  'Caused by Septoria lycopersici.','Small circular spots with dark borders.','Remove infected leaves, apply fungicide.',                   'Medium',  0),
('Tomato_Spider_mites',      'Tomato',  'Spider Mites (Two-spotted mite)','Pest infestation.','Yellow stippling on leaves.',           'Apply miticide or neem oil spray.',                           'Low',     0),
('Potato_healthy',           'Potato',  'Healthy',             'No disease detected.',           'Plant looks green and healthy.',       'No treatment needed.',                                        'Healthy', 1),
('Potato_Early_blight',      'Potato',  'Early Blight',        'Caused by Alternaria solani.',   'Brown spots with concentric rings.',   'Apply chlorothalonil or mancozeb fungicide.',                  'Medium',  0),
('Potato_Late_blight',       'Potato',  'Late Blight',         'Caused by Phytophthora infestans.','Dark lesions on leaves and stems.',  'Remove infected plants. Apply metalaxyl fungicide.',           'High',    0),
('Corn_healthy',             'Corn',    'Healthy',             'No disease detected.',           'Green, upright leaves.',               'No treatment needed.',                                        'Healthy', 1),
('Corn_Common_rust',         'Corn',    'Common Rust',         'Caused by Puccinia sorghi.',     'Rusty-brown pustules on leaf surfaces.','Apply propiconazole or azoxystrobin fungicide.',               'Medium',  0),
('Corn_Northern_Leaf_Blight','Corn',    'Northern Leaf Blight','Caused by Exserohilum turcicum.','Long grayish lesions on leaves.',      'Use resistant varieties, apply strobilurin fungicides.',       'High',    0),
('Apple_healthy',            'Apple',   'Healthy',             'No disease detected.',           'Shiny, green leaves.',                 'No treatment needed.',                                        'Healthy', 1),
('Apple_scab',               'Apple',   'Apple Scab',          'Caused by Venturia inaequalis.', 'Olive-green or brown scabs on leaves.','Apply myclobutanil or captan fungicide at bud break.',         'Medium',  0),
('Apple_Black_rot',          'Apple',   'Black Rot',           'Caused by Botryosphaeria obtusa.','Purple spots enlarging to brown rot.', 'Prune infected branches. Apply fungicide.',                   'High',    0),
('Grape_healthy',            'Grape',   'Healthy',             'No disease detected.',           'Vibrant green leaves.',                'No treatment needed.',                                        'Healthy', 1),
('Grape_Black_rot',          'Grape',   'Black Rot',           'Caused by Guignardia bidwellii.','Brown lesions, black mummified berries.','Apply mancozeb before bloom.',                              'High',    0),
('Pepper_healthy',           'Pepper',  'Healthy',             'No disease detected.',           'Glossy, dark green leaves.',           'No treatment needed.',                                        'Healthy', 1),
('Pepper_Bacterial_spot',    'Pepper',  'Bacterial Spot',      'Caused by Xanthomonas campestris.','Water-soaked spots on leaves.',      'Apply copper-based bactericide. Avoid overhead irrigation.',   'Medium',  0);
