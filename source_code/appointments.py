from database import get_db_connection
from datetime import datetime

def book_appointment():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        patient_id_input = input("Enter patient ID: ")
        try:
            patient_id = int(patient_id_input)
        except ValueError:
            print("Please enter a valid patient ID (number).")
            continue
        cursor.execute("SELECT 1 FROM patients WHERE patient_id=%s", (patient_id,))
        if cursor.fetchone() is None:
            print("Patient ID not found. Please enter a valid patient ID.")
            continue
        break
    
    while True:
        doctor_id_input = input("Enter doctor ID: ")
        try:
            doctor_id = int(doctor_id_input)
        except ValueError:
            print("Please enter a valid doctor ID (number).")
            continue
        cursor.execute("SELECT 1 FROM doctors WHERE doctor_id=%s", (doctor_id,))
        if cursor.fetchone() is None:
            print("Doctor ID not found. Please enter a valid doctor ID.")
            continue
        break
        
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
    today = datetime.now().date()
    cursor.execute("""SELECT a.appointment_id, p.name, d.name, a.appointment_date
                      FROM appointments a
                      JOIN patients p ON a.patient_id = p.patient_id
                      JOIN doctors d ON a.doctor_id = d.doctor_id
                      WHERE a.appointment_date >= %s
                      ORDER BY a.appointment_date""", (today,))
    rows = cursor.fetchall()
    print("-" * 60)
    if not rows:
        print("No upcoming appointments.")
    else:
        for appointment_id, patient_name, doctor_name, appointment_date in rows:
            print(f"{appointment_id:>4} | {patient_name:<20} | {doctor_name:<20} | {appointment_date}")
    print("-" * 60)
    db.close()

def update_appointment():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        appointment_id_input = input("Enter appointment ID to update: ").strip()
        try:
            appointment_id = int(appointment_id_input)
        except ValueError:
            print("Please enter a valid appointment ID (number).")
            continue
        cursor.execute("SELECT 1 FROM appointments WHERE appointment_id=%s", (appointment_id,))
        if cursor.fetchone() is None:
            print("Appointment ID not found. Please enter a valid appointment ID.")
            continue
        break

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
    while True:
        appointment_id_input = input("Enter appointment ID to delete: ").strip()
        try:
            appointment_id = int(appointment_id_input)
        except ValueError:
            print("Please enter a valid appointment ID (number).")
            continue
        cursor.execute("SELECT 1 FROM appointments WHERE appointment_id=%s", (appointment_id,))
        if cursor.fetchone() is None:
            print("Appointment ID not found. Please enter a valid appointment ID.")
            continue
        break

    cursor.execute("DELETE FROM appointments WHERE appointment_id=%s", (appointment_id,))
    db.commit()
    db.close()
    print("🗑 Appointment deleted successfully!")
