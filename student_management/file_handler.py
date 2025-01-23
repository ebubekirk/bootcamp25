import error_handler

def read_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()
            return eval(data)
    except FileNotFoundError:
        return error_handler.NoDatabaseFound()
    except (SyntaxError, ValueError):
        return error_handler.DatabaseReadError()

def write_students(students):
    try:
        with open("students.txt", "w") as file:
            file.write(str(students))
        return 1
    except ValueError:
        return error_handler.DatabaseUpdateError()

