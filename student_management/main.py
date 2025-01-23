from student_operations import add_student, view_students, update_student, delete_student

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
