from database import get_db_connection
def add_patient():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        name = input("Enter patient name: ").strip()
        
        isDIGIT=False
        if name=="":
            print("name cannot be empty")
            continue
        for i in name:
            if i.isdigit()==True:
                isDIGIT=True
                print("please enter a valid name(no number)")
                continue
        if not isDIGIT:
            break 

    while True:
        age_input = input("Enter age: ")
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Please enter a valid age.")
       
    while True:
        gender = input("Enter gender (Male/Female): ").strip().capitalize()
        if gender in ["Male", "Female"]:
            break
        else:
            print("Invalid gender. Please enter 'Male' or 'Female'.")

    # enforce contact number exactly 10 digits (or optional)
    while True:
        contact = input("Enter contact number (optional):").strip()
        if contact == "":
            contact = None
            break
        elif contact.isdigit() and len(contact) == 10:
            break
        elif contact.isdigit() and len(contact) != 10:
            print("Contact number must be exactly 10 digits. Please enter a valid 10-digit number, or leave blank to skip.")
        else:
            print("Invalid contact number. Please enter digits only (10 digits), or leave blank to skip.")

    cursor.execute(
        "INSERT INTO patients (name, age, gender, contact) VALUES (%s, %s, %s, %s)",
        (name, age, gender, contact)
    )
    db.commit()
    db.close()
    print("✅ Patient added successfully!")

def view_patients():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM patients")
    print("-" * 60)
    for row in cursor.fetchall():
        print(row)
    print("-" * 60)
    db.close()

def update_patient():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        patient_id = input("Enter patient ID to update: ")
        try:
            patient_id_int = int(patient_id)
        except ValueError:
            print("Please enter a valid patient ID.")
            continue

        cursor.execute("SELECT * FROM patients WHERE patient_id=%s", (patient_id_int,))
        row = cursor.fetchone()
        if row:
            int_patient_id = patient_id_int  # use integer id for subsequent queries
            print(f"Found patient: {row}")
            break
        else:
            print("Patient ID not found. Please enter a valid patient ID.")

    while True:
        name = input("Enter new name: ").strip()
        isDIGIT = False
        if name == "":
            print("Name cannot be empty")
            continue
        for i in name:
            if i.isdigit():
                isDIGIT = True
                print("Please enter a valid name (no number)")
                break
        if not isDIGIT:
            break

    while True:
        age_input = input("Enter new age: ")
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Please enter a valid age.")

    while True:
        gender = input("Enter new gender (Male/Female): ").strip().capitalize()
        if gender in ["Male", "Female"]:
            break
        else:
            print("Invalid gender. Please enter 'Male' or 'Female'.")

    while True:
        contact = input("Enter new contact number (optional):").strip()
        if contact == "":
            contact = None
            break
        elif contact.isdigit() and len(contact) >= 7:
            break
        else:
            print("Invalid contact number. Please enter a valid number (at least 7 digits), or leave blank to skip.")

    cursor.execute(
        "UPDATE patients SET name=%s, age=%s, gender=%s, contact=%s WHERE patient_id=%s",
        (name, age, gender, contact, int_patient_id)
    )
    db.commit()
    db.close()
    print("✅ Patient updated successfully!")

def delete_patient():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        patient_id = input("Enter patient ID to update: ")
        try:
            int_patient_id = int(patient_id)
        except ValueError:
            print("Please enter a valid patient ID.")
            continue

        cursor.execute("SELECT 1 FROM patients WHERE patient_id=%s", (int_patient_id,))
        if cursor.fetchone() is None:
            print(f"Patient ID {int_patient_id} not found. Please enter an existing patient ID.")
            continue
        break
    cursor.execute("DELETE FROM patients WHERE patient_id=%s", (int_patient_id,))
    db.commit()
    db.close()
    print("🗑 Patient deleted successfully!")
