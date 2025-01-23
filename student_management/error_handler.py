def handle_error(error):
    print(f"An error occurred: {error}")

def NoDatabaseFound():
    print("No database found!")
    return {}

def DatabaseReadError():
    print("There was an error reading from the database!")
    return {}

def DatabaseUpdateError():
    print("Database cannot be updated!")
    return 0
