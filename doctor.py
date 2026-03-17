from db import connect
def add_doctor(name, specialization):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO doctors (name, specialization) VALUES (?, ?)",
        (name, specialization)
    )
    conn.commit()
    conn.close()
def view_doctors():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    data = cursor.fetchall()
    conn.close()
    return data