import pandas as pd
from pathlib import Path
import database
from datetime import datetime

def export_csv():
    conn = database.get_connection()
    df = pd.read_sql_query("SELECT a.id, s.name, s.roll_no, a.date, a.time FROM attendance a JOIN students s ON a.student_id = s.id", conn)
    export_dir = Path(__file__).resolve().parent / "exports"
    export_dir.mkdir(exist_ok=True)
    file_path = export_dir / f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(file_path, index=False)
    conn.close()
    print(f"Attendance exported to {file_path}")

if __name__ == "__main__":
    export_csv()
