import cv2
import os
from datetime import datetime
from pathlib import Path
import database

def register_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    folder_name = f"{name}_{roll_no}"
    save_dir = Path(__file__).resolve().parent / "dataset" / folder_name
    save_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0
    print("Press SPACE to capture an image, ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Registration - Capture Faces", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            img_path = save_dir / f"{name}_{count}.jpg"
            cv2.imwrite(str(img_path), frame)
            print(f"Captured {img_path}")
            count += 1
            if count >= 30:
                print("Captured 30 images, exiting.")
                break
    cap.release()
    cv2.destroyAllWindows()

    database.add_student(name, roll_no, save_dir)
    print("Student registered successfully.")

if __name__ == "__main__":
    database.init_db()
    register_student()
