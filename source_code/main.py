from patients import add_patient, view_patients, update_patient, delete_patient
from doctors import add_doctor, view_doctors, update_doctor, delete_doctor
from appointments import book_appointment, view_appointments, update_appointment, delete_appointment

first_run=True
while True:
    if first_run:
        first_run = False
    else:
        input("\nPress Enter to continue...")
    print("\n" + "="*40)
    print("      🏥 Hospital Management System      ")
    print("="*40)
    print("1. ➕ Add Patient")
    print("2. 📋 View Patients")
    print("3. ✏️  Update Patient")
    print("4. ❌ Delete Patient")
    print("5. ➕ Add Doctor")
    print("6. 📋 View Doctors")
    print("7. ✏️  Update Doctor")
    print("8. ❌ Delete Doctor")
    print("9. 📅 Book Appointment")
    print("10.📋 View Appointments")
    print("11.✏️  Update Appointment")
    print("12.❌ Delete Appointment")
    print("13.🚪 Exit")
    print("="*40)

    choice = input("👉 Enter your choice: ")

    try:
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            add_doctor()
        elif choice == "6":
            view_doctors()
        elif choice == "7":
            update_doctor()
        elif choice == "8":
            delete_doctor()
        elif choice == "9":
            book_appointment()
        elif choice == "10":
            view_appointments()
        elif choice == "11":
            update_appointment()
        elif choice == "12":
            delete_appointment()
        elif choice == "13":
            break
        else:
            print("❌ Invalid choice!")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
