# fix_the_functions.py

# runtime: define the function before calling it.
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


print_header()


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        # semantic: return the calculated total instead of always returning 0.
        total = failed * minutes
        return total
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# runtime: use the exact parameter name, username.
print(login_line(username="sara", failed=4))

# semantic: print the returned line so it appears in the output.
print(login_line("omar", 1))
