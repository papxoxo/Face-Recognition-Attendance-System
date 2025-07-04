import face_recognition
import pickle
import os
from pathlib import Path

DATASET_DIR = Path(__file__).resolve().parent / "dataset"
ENCODINGS_PATH = Path(__file__).resolve().parent / "encodings.pkl"

def train():
    known_encodings = []
    known_names = []

    for student_dir in DATASET_DIR.iterdir():
        if not student_dir.is_dir():
            continue
        name = student_dir.name
        for img_path in student_dir.glob("*.jpg"):
            image = face_recognition.load_image_file(img_path)
            boxes = face_recognition.face_locations(image, model="hog")
            encodings = face_recognition.face_encodings(image, boxes)
            for enc in encodings:
                known_encodings.append(enc)
                known_names.append(name)

    print(f"Encoded {len(known_encodings)} faces.")
    data = {"encodings": known_encodings, "names": known_names}
    with open(ENCODINGS_PATH, "wb") as f:
        pickle.dump(data, f)
    print(f"Encodings saved to {ENCODINGS_PATH}")

if __name__ == "__main__":
    train()
