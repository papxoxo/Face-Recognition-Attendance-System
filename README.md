# Face Recognition Based Attendance System

An offline, privacy-focused face recognition-based attendance system built using **Python**, **OpenCV**, **face_recognition**, and **Tkinter** — now with ✨ **voice feedback** for a smart AI touch!

---

## 🚀 Features

- 🧠 Real-time face detection & recognition
- 👨‍🎓 Student registration with image capture
- 🧾 Attendance logging with date & time
- 🧠 Facial encoding with `face_recognition` library
- 🔊 **Voice feedback** using `pyttsx3`
- 📁 CSV export for attendance logs
- 💻 GUI built with Tkinter
- 🔐 Local SQLite database (no cloud, no leaks!)
- 🛡️ Privacy-respecting — dataset never pushed to GitHub

---

## 🛠️ Tech Stack

| Area              | Tech Used               |
|-------------------|-------------------------|
| Programming       | Python 3.x              |
| GUI               | Tkinter                 |
| Face Recognition  | face_recognition, OpenCV|
| TTS (Voice)       | pyttsx3                 |
| Database          | SQLite3                 |
| Data Handling     | Pickle, CSV             |

---

## 🖥️ How It Works

1. **Register Student**  
   Capture face images and store them in a local dataset.

2. **Train Model**  
   Convert all faces to encodings and save to `encodings.pkl`.

3. **Mark Attendance**  
   Run webcam → Detect face → Match encoding → Mark attendance in database and give voice feedback.

---

## 💾 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/face-attendance-system.git
   cd face-attendance-system

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
│
├── dataset/              # Local face images (ignored)
├── exports/              # CSV logs
├── encodings.pkl         # Facial encodings (ignored)
├── main.py               # GUI entry point
├── registration.py       # Image capture & student add
├── train_model.py        # Encodes all face data
├── mark_attendance.py    # Runs webcam & marks attendance
├── database.py           # Handles SQLite logic
├── .gitignore
└── README.md

```

## Notes

- Ensure good lighting during registration and attendance.
- The default tolerance threshold is 0.6 (can be tuned in `mark_attendance.py`).
- For better accuracy, you can switch `model="hog"` to `model="cnn"` if you have a GPU and dlib with CUDA.
