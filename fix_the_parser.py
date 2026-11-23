"""Corrected log-line parser for Silver Bug Hunt 9."""

LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: the time has five characters, so include index 4.
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: lower() returns a new string, so keep the returned value.
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: normalize case because the log may use uppercase FAILED.
    return "failed" in line.lower()


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings are immutable, so construct and return a new string.
    return "*" + user[1:]


# runtime: len() is a built-in function, not a string method.
print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
print(f"Length: {len(LINE)}")
