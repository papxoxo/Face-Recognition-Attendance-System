import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "attendance.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE,
            folder_path TEXT NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            time TEXT,
            status TEXT DEFAULT 'Present',
            FOREIGN KEY(student_id) REFERENCES students(id)
        );
    """)
    conn.commit()
    conn.close()

def add_student(name: str, roll_no: str, folder_path: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name, roll_no, folder_path) VALUES (?,?,?)",
                (name, roll_no, str(folder_path)))
    conn.commit()
    conn.close()

def get_student_by_roll(roll_no: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cur.fetchone()
    conn.close()
    return student

def log_attendance(student_id: int, date_str: str, time_str: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance(student_id, date, time) VALUES (?,?,?)",
                (student_id, date_str, time_str))
    conn.commit()
    conn.close()

def attendance_exists(student_id: int, date_str: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM attendance WHERE student_id=? AND date=?",
                (student_id, date_str))
    exists = cur.fetchone() is not None
    conn.close()
    return exists
