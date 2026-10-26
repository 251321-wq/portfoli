# Decide whether a login is allowed based on lockout and credentials.
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Username: ")
failed = int(input("Failed attempts: "))
password = input("Password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password == STORED_PASSWORD:
    print("Access granted.")
else:
    print(f"Access denied. Attempts left: {MAX_FAILED - failed - 1}")
