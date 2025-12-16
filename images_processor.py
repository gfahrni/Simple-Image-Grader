import os
import re
from helpers.paths import DATA_FOLDER

def scan_images_folder(folder="images"):
    """
    Scan the given folder for images named like '003_p1.jpg'.
    Returns a list of tuples: (patient_id, image_number, filename)
    """
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return []

    pattern = re.compile(r"(\d+)_p(\d+)\.\w+")  # matches '003_p1.jpg', '012_p2.png', etc.

    images_list = []

    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match:
            patient_id = int(match.group(1))
            image_number = int(match.group(2))
            images_list.append((patient_id, image_number, filename))

    return images_list

def get_patient_images(patient_id):
    """
    Returns a list of image filenames for a given patient, sorted by image number.
    """
    folder = os.path.join(DATA_FOLDER, "images") # Path to 'images' folder
    pattern = re.compile(r"(\d+)_p(\d+)\.\w+")
    images = []

    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match and int(match.group(1)) == patient_id:
            image_number = int(match.group(2))
            images.append((image_number, os.path.join(folder, filename)))

    # Sort by image number
    images.sort(key=lambda x: x[0])
    return [img[1] for img in images]  # Return full paths

# Test run only when executed directly
if __name__ == "__main__":
    images = scan_images_folder()
    print("--- Scanned Images ---")
    for img in images:
        print(f"Patient {img[0]:03d}, Image {img[1]} → {img[2]}")
    print(f"Total images found: {len(images)}")
