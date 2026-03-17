from db import connect
def book_appointment(patient_id, doctor_id, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (patient_id, doctor_id, date) VALUES (?, ?, ?)",
        (patient_id, doctor_id, date)
    )
    conn.commit()
    conn.close()
def view_appointments():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT a.id, p.name, d.name, a.date
    FROM appointments a
    JOIN patients p ON a.patient_id = p.id
    JOIN doctors d ON a.doctor_id = d.id
    """)
    data = cursor.fetchall()
    conn.close()
    return data