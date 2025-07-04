import tkinter as tk
from tkinter import messagebox
import subprocess
import database

def run_registration():
    subprocess.run(["python3", "registration.py"])

def run_training():
    subprocess.run(["python", "train_model.py"])

def run_attendance():
    subprocess.run(["python", "mark_attendance.py"])

def run_export():
    subprocess.run(["python", "export_attendance.py"])

def init_db():
    database.init_db()
    messagebox.showinfo("DB", "Database initialized")

root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x300")

tk.Button(root, text="Initialize Database", width=25, command=init_db).pack(pady=10)
tk.Button(root, text="Register Student", width=25, command=run_registration).pack(pady=10)
tk.Button(root, text="Train Model", width=25, command=run_training).pack(pady=10)
tk.Button(root, text="Mark Attendance", width=25, command=run_attendance).pack(pady=10)
tk.Button(root, text="Export Attendance CSV", width=25, command=run_export).pack(pady=10)

root.mainloop()
