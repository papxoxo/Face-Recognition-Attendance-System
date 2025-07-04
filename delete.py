import database

def delete_student_by_roll(roll_no):
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()

delete_student_by_roll("105")
