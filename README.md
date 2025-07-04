# Face Recognition Based Attendance System

## Setup

1. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main application:
```bash
python main.py
```

## Usage

- **Initialize Database**: Creates required tables.
- **Register Student**: Capture 30 face images for a new student via webcam.
- **Train Model**: Encode all faces and save `encodings.pkl`.
- **Mark Attendance**: Recognize faces live and log attendance.
- **Export Attendance CSV**: Save attendance logs to a timestamped CSV file in `exports/`.

## Project Structure
```
face_attendance_system/
├── dataset/               # Captured face images
├── encodings.pkl          # Saved face encodings
├── db/attendance.db       # SQLite database
├── exports/               # CSV reports
├── *.py                   # Source code
└── README.md
```

## Notes

- Ensure good lighting during registration and attendance.
- The default tolerance threshold is 0.6 (can be tuned in `mark_attendance.py`).
- For better accuracy, you can switch `model="hog"` to `model="cnn"` if you have a GPU and dlib with CUDA.
