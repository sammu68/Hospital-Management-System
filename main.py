from db import create_tables
from patient import add_patient, view_patients
from doctor import add_doctor, view_doctors
from appointment import book_appointment, view_appointments
def menu():
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Doctor")
    print("4. View Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("0. Exit")
create_tables()
while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        add_patient(name, age, gender)
    elif choice == "2":
        print(view_patients())
    elif choice == "3":
        name = input("Doctor Name: ")
        spec = input("Specialization: ")
        add_doctor(name, spec)
    elif choice == "4":
        print(view_doctors())
    elif choice == "5":
        pid = int(input("Patient ID: "))
        did = int(input("Doctor ID: "))
        date = input("Date (YYYY-MM-DD): ")
        book_appointment(pid, did, date)
    elif choice == "6":
        print(view_appointments())
    elif choice == "0":
        break
    else:
        print("Invalid choice")