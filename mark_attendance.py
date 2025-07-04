import face_recognition
import cv2
import pickle
from datetime import datetime
from pathlib import Path
import database

ENCODINGS_PATH = Path(__file__).resolve().parent / "encodings.pkl"
THRESHOLD = 0.6

def recognize_and_mark():
    database.init_db()
    with open(ENCODINGS_PATH, "rb") as f:
        data = pickle.load(f)

    print("Starting webcam for attendance. Press ESC to exit.")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)

        for box, encoding in zip(boxes, encodings):
            matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=THRESHOLD)
            face_dist = face_recognition.face_distance(data["encodings"], encoding)

            name = "Unknown"
            best_match_index = None
            if len(face_dist) > 0:
                best_match_index = face_dist.argmin()

            if best_match_index is not None and matches[best_match_index]:
                name = data["names"][best_match_index]
                # name format is name_roll
                roll_no = name.split("_")[-1]
                student = database.get_student_by_roll(roll_no)
                if student:
                    student_id = student[0]
                    date_str = datetime.now().strftime("%Y-%m-%d")
                    time_str = datetime.now().strftime("%H:%M:%S")
                    if not database.attendance_exists(student_id, date_str):
                        database.log_attendance(student_id, date_str, time_str)
                        print(f"Marked attendance for {name} at {time_str}")
                    else:
                        print(f"{name} already marked today.")

            (top, right, bottom, left) = box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_and_mark()
