# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Fix 1 (syntax): add the missing colon to the if statement.
if len(password) < MIN_LENGTH:
    print("- Too short.")
# Fix 2 (semantic): use a separate if so both warnings can appear.
if password == username:
    print("- Same as the username.")

# Fix 3 (semantic): check 16+ before 12+ to make 'long' reachable.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Fix 4 (semantic): print the length outside the else for every input.
print(f"Length: {len(password)} ({strength})")
