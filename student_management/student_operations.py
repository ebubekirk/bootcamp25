import file_handler
from error_handler import handle_error

def add_student():
    students = file_handler.read_students()
    new_student = {
        input("Enter Student ID: "): {
            "name": input("Enter Student Name: "),
            "age": input("Enter Student Age: "),
            "grade": input("Enter Student Grade: ")
        }
    }
    students.update(new_student)
    file_handler.write_students(students)
    print("Student added successfully!")


def view_students():
    students = file_handler.read_students()
    print(students)
    if not students:
        print("No students found.")
    else:
        print("\n--- Student Records ---")
        for studentID in students:
            print(f"ID: {studentID}, Name: {students[studentID]['name']}, Age: {students[studentID]['age']}, Grade: {students[studentID]['grade']}")


def update_student():
    students = file_handler.read_students()
    studentID = input("Enter Student ID to update: ")
    if studentID in students:
        print (students[studentID])
        students[studentID]["name"] = input("Enter new name: ")
        students[studentID]["age"] = input("Enter new age: ")
        students[studentID]["grade"] = input("Enter new grade: ")
        
        if file_handler.write_students(students):
            print("Student updated successfully!")
        else:
            print("Student cannot be updated due to write error!")
    else:
        print("Student not found.")

def delete_student():
    students = file_handler.read_students()
    studentID = input("Enter Student ID to delete: ")
    if studentID in students:
        del students[studentID]
        if file_handler.write_students(students):
            print("Student deleted successfully!")
        else:
            print("Student cannot be deleted due to write error!")
    else:
        print("Student not found.")
