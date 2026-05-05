import os
import shutil
import random
from sklearn.model_selection import train_test_split

# =========================
# 🔹 PATHS (EDIT IF NEEDED)
# =========================
plant_village_path = r"dataset/PlantVillage"
plant_doc_path = r"dataset/PlantDoc"
output_path = "dataset/processed"

# =========================
# 🔹 SETTINGS
# =========================
IMG_EXTENSIONS = (".jpg", ".jpeg", ".png")
RANDOM_SEED = 42
MAX_IMAGES_PER_CLASS = 1500   # limit to balance dataset (optional)

random.seed(RANDOM_SEED)

# =========================
# 🔹 CLEAN CLASS NAME
# =========================
def clean_name(name):
    name = name.replace("___", "_")
    name = name.replace(" ", "_")
    name = name.replace("(", "").replace(")", "")
    name = name.replace("-", "_")
    return name.strip()

# =========================
# 🔹 LOAD IMAGES
# =========================
data = {}

def load_images(base_path):
    if not os.path.exists(base_path):
        print(f"[ERROR] Path not found: {base_path}")
        return

    for class_name in os.listdir(base_path):
        class_path = os.path.join(base_path, class_name)

        if not os.path.isdir(class_path):
            continue

        clean_class = clean_name(class_name)

        if clean_class not in data:
            data[clean_class] = []

        for img in os.listdir(class_path):
            if img.lower().endswith(IMG_EXTENSIONS):
                img_path = os.path.join(class_path, img)
                data[clean_class].append(img_path)

# =========================
# 🔹 LOAD DATASETS
# =========================
print("Loading datasets...")
load_images(plant_village_path)
load_images(plant_doc_path)

# =========================
# 🔹 CREATE OUTPUT FOLDERS
# =========================
for split in ["train", "val", "test"]:
    for class_name in data.keys():
        os.makedirs(os.path.join(output_path, split, class_name), exist_ok=True)

# =========================
# 🔹 SPLIT + COPY
# =========================
print("Processing & splitting...")

for class_name, images in data.items():

    if len(images) == 0:
        continue

    # 🔥 Balance dataset (optional but recommended)
    if len(images) > MAX_IMAGES_PER_CLASS:
        images = random.sample(images, MAX_IMAGES_PER_CLASS)

    train, temp = train_test_split(images, test_size=0.3, random_state=RANDOM_SEED)
    val, test = train_test_split(temp, test_size=0.5, random_state=RANDOM_SEED)

    for split_name, split_data in zip(["train", "val", "test"], [train, val, test]):
        for img_path in split_data:
            filename = os.path.basename(img_path)

            # 🔥 Avoid duplicate filename overwrite
            dest_path = os.path.join(output_path, split_name, class_name, filename)

            counter = 1
            while os.path.exists(dest_path):
                name, ext = os.path.splitext(filename)
                new_name = f"{name}_{counter}{ext}"
                dest_path = os.path.join(output_path, split_name, class_name, new_name)
                counter += 1

            shutil.copy(img_path, dest_path)

print("Dataset cleaned, merged, and split successfully!")