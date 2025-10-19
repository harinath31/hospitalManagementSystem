from database import get_db_connection
specializations = [
        {"id": 1, "name": "Cardiology"},
        {"id": 2, "name": "Neurology"},
        {"id": 3, "name": "Orthopedics"},
        {"id": 4, "name": "Pediatrics"},
        {"id": 5, "name": "General Medicine"}
    ]

def add_doctor():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        name = input("Enter doctor name:")
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
    print("Available specializations:")
    for spec in specializations:
        print(f"{spec['id']}. {spec['name']}")
    while True:
        try:
            spec_choice = int(input("Select specialization (enter number): "))
            spec = next((s for s in specializations if s["id"] == spec_choice), None)
            if spec:
                specialization = spec["name"]
                break
            else:
                print("Please select a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        contact = input("Enter contact number (optional, 10 digits): ").strip()
        if contact == "":
            contact = None
            break
        elif contact.isdigit() and len(contact) == 10:
            break
        elif contact.isdigit() and len(contact) != 10:
            print("Contact number must be exactly 10 digits. Please enter a valid 10-digit number, or leave blank to skip.")
        else:
            print("Invalid contact number. Please enter exactly 10 digits, or leave blank to skip.")
    cursor.execute("INSERT INTO doctors (name, specialization, contact) VALUES (%s, %s, %s)",
                   (name, specialization, contact))
    db.commit()
    db.close()
    print("✅ Doctor added successfully!")

def view_doctors():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM doctors")
    print("-" * 60)
    for row in cursor.fetchall():
        print(row)
    print("-" * 60)
    db.close()

def update_doctor():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        doctor_id = input("Enter doctor ID to update: ")
        try:
            doctor_id_int = int(doctor_id)
        except ValueError:
            print("please enter a valid doctor id")
            continue

        cursor.execute("SELECT * FROM doctors WHERE doctor_id=%s", (doctor_id_int,))
        row = cursor.fetchone()
        if row:
            doctor_id = doctor_id_int  # use integer id for subsequent queries
            print(f"Found doctor: {row}")
            break
        else:
            print("Doctor ID not found. Please enter a valid doctor id.")
    while True:
        name = input("Enter new name: ")      
        
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
    print("Available specializations:")
    for spec in specializations:
        print(f"{spec['id']}. {spec['name']}")
    while True:
        try:
            spec_choice = int(input("Select new specialization (enter number): "))
            spec = next((s for s in specializations if s["id"] == spec_choice), None)
            if spec:
                specialization = spec["name"]
                break
            else:
                print("Please select a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        contact = input("Enter new contact: ")
        if contact.isdigit() and len(contact) >= 7:
            break
        else:
            print("Invalid contact number. Please enter a valid number (at least 7 digits).")
    cursor.execute("UPDATE doctors SET name=%s, specialization=%s, contact=%s WHERE doctor_id=%s",
                   (name, specialization, contact, doctor_id))
    db.commit()
    db.close()
    print("✅ Doctor updated successfully!")

def delete_doctor():
    db = get_db_connection()
    cursor = db.cursor()
    while True:
        doctor_id = input("Enter doctor ID to delete: ")
        try:
            doctor_id_int = int(doctor_id)
        except ValueError:
            print("please enter a valid doctor id")
            continue

        cursor.execute("SELECT 1 FROM doctors WHERE doctor_id=%s", (doctor_id_int,))
        if cursor.fetchone():
            doctor_id = doctor_id_int
            print(f"Found doctor with ID {doctor_id}.")
            break
        else:
            print("Doctor ID not found. Please enter a valid doctor id.")
    cursor.execute("DELETE FROM doctors WHERE doctor_id=%s", (doctor_id,))
    db.commit()
    db.close()
    print(" Doctor deleted successfully!")
