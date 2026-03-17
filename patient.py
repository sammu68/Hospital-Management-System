from db import connect

def add_patient(name, age, gender):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO patients (name, age, gender) VALUES (?, ?, ?)",
        (name, age, gender)
    )

    conn.commit()
    conn.close()

def view_patients():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()

    conn.close()
    return data