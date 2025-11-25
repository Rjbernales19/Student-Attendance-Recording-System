# === STUDENT ATTENDANCE RECORDING SYSTEM ===

students = ["Bernales", "Inzo", "Sumahon", "Sebuco", "Castanares"]
attendance = {}

while True:
    print("\n=== STUDENT ATTENDANCE RECORDING SYSTEM ===")
    print("Select Role:")
    print("1. Teacher")
    print("2. Class Adviser / Coordinator")
    print("3. Exit Program")

    role = input("Enter your role (1, 2, or 3): ")

    # ---------------- TEACHER MENU ---------------- #
    if role == "1":
        while True:
            print("\n--- TEACHER MENU ---")
            print("1. Mark Attendance")
            print("2. View Attendance Record")
            print("3. Back to Main Menu")

            option = input("Choose an option (1, 2, or 3): ")

            if option == "1":
                date = input("Enter date (e.g. Nov 5, 2025): ")
                attendance[date] = {}

                for name in students:
                    status = input(f"Is {name} present? (P/A): ").strip().upper()
                    attendance[date][name] = "Present" if status == "P" else "Absent"

                with open("attendance_record.txt", "a") as file:
                    file.write(f"\n=== Attendance for {date} ===\n")
                    for name, status in attendance[date].items():
                        file.write(f"{name}: {status}\n")

                print(f"\nAttendance for {date} saved successfully!")

            elif option == "2":
                print("\n=== VIEW ATTENDANCE RECORD ===")
                try:
                    with open("attendance_record.txt", "r") as file:
                        print(file.read())
                except FileNotFoundError:
                    print("No attendance record found yet.")

            elif option == "3":
                print("Returning to main menu...")
                break

            else:
                print("Invalid option. Please try again.")

    # ---------------- CLASS ADVISER MENU ---------------- #
    elif role == "2":
        while True:
            print("\n--- CLASS ADVISER MENU ---")
            print("1. View All Attendance Records")
            print("2. View Summary per Student")
            print("3. Back to Main Menu")

            option = input("Choose an option (1, 2, or 3): ")

            if option == "1":
                print("\n=== ALL ATTENDANCE RECORDS ===")
                try:
                    with open("attendance_record.txt", "r") as file:
                        print(file.read())
                except FileNotFoundError:
                    print("No attendance records found.")

            elif option == "2":
                print("\n=== SUMMARY PER STUDENT ===")
                try:
                    with open("attendance_record.txt", "r") as file:
                        lines = file.readlines()
                except FileNotFoundError:
                    print("No attendance records found.")
                    lines = []

                summary = {name: {"Present": 0, "Absent": 0} for name in students}

                for line in lines:
                    for name in students:
                        if line.startswith(name):
                            if "Present" in line:
                                summary[name]["Present"] += 1
                            elif "Absent" in line:
                                summary[name]["Absent"] += 1

                for name in students:
                    print(f"{name}: Present = {summary[name]['Present']}, Absent = {summary[name]['Absent']}")

            elif option == "3":
                print("Returning to main menu...")
                break

            else:
                print("Invalid option. Please try again.")

    elif role == "3":
        print("Exiting the program... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")