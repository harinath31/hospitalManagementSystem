from database import get_db_connection
from datetime import datetime

def book_appointment():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        patient_id = input("Enter patient ID: ")
        try:
            patient_id = int(patient_id)
            break
        except ValueError:
            print("Please enter a valid patient ID (number).")
            

    while True:
        doctor_id_input = input("Enter doctor ID: ")
        try:
            doctor_id = int(doctor_id_input)
            break            
        except ValueError:
            print("Please enter a valid doctor ID (number).")
        
    while True:
        date_str = input("Enter appointment date (YYYY-MM-DD): ")
        try:
            appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if appointment_date < datetime.now().date():
                print("Appointment date cannot be in the past. Please enter today or a future date.")
            else:
                break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
    appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)",
                   (patient_id, doctor_id, appointment_date))
    db.commit()
    db.close()
    print("✅ Appointment booked successfully!")

def view_appointments():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""SELECT a.appointment_id, p.name, d.name, a.appointment_date
                      FROM appointments a
                      JOIN patients p ON a.patient_id = p.patient_id
                      JOIN doctors d ON a.doctor_id = d.doctor_id""")    
    print("-" * 60)
    for row in cursor.fetchall():
        print(row)
    print("-" * 60)
    db.close()

def update_appointment():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        appointment_id = input("Enter appointment ID to update: ")
        try:
            int(appointment_id)            
            break
        except ValueError:
            print("Please enter a valid appointment ID (number).")

    while True:
        patient_id = input("Enter new patient ID: ").strip()
        if patient_id == "":
            patient_id = None
            break
        try:
            patient_id = int(patient_id)
            cursor.execute("SELECT 1 FROM patients WHERE patient_id=%s", (patient_id,))
            if cursor.fetchone() is None:
                print("Patient ID not found. Please enter a valid patient ID.")
                continue
            break
        except ValueError:
            print("Please enter a valid patient ID (number).")

    while True:
        doctor_id = input("Enter new doctor ID: ").strip()
        if doctor_id == "":
            doctor_id = None
            break
        try:
            doctor_id = int(doctor_id)
            cursor.execute("SELECT 1 FROM doctors WHERE doctor_id=%s", (doctor_id,))
            if cursor.fetchone() is None:
                print("Doctor ID not found. Please enter a valid doctor ID.")
                continue
            break
        except ValueError:
            print("Please enter a valid doctor ID (number).")

    while True:
        new_date_str = input("Enter new appointment date (YYYY-MM-DD): ").strip()
        if new_date_str == "":
            new_date = None
            break
        try:
            new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()
            if new_date < datetime.now().date():
                print("Appointment date cannot be in the past. Please enter today or a future date.")
                continue
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    cursor.execute("UPDATE appointments SET patient_id=%s, doctor_id=%s, appointment_date=%s WHERE appointment_id=%s",
                   (patient_id, doctor_id, new_date, appointment_id))
    db.commit()
    db.close()

    print("✅ Appointment updated successfully!")

def delete_appointment():
    db = get_db_connection()
    cursor = db.cursor()
    appointment_id = int(input("Enter appointment ID to delete: "))
    cursor.execute("DELETE FROM appointments WHERE appointment_id=%s", (appointment_id,))
    db.commit()
    db.close()
    print("🗑 Appointment deleted successfully!")
