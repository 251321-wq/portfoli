"""Check usernames against the course username policy."""

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return the username without surrounding whitespace and in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character that is not a letter, digit, or underscore."""
    for character in username:
        if not (character.isalpha() or character.isdecimal() or character == "_"):
            return character
    return ""


def policy_problem(username):
    """Return the first username policy problem, or an empty string."""
    if len(username) < MIN_LENGTH or len(username) > MAX_LENGTH:
        return "length must be 3 to 12."

    if not username[0].isalpha():
        return "it must start with a letter."

    character = bad_character(username)
    if character != "":
        return f"the character {character} is not allowed."

    return ""


def main():
    """Read, clean, and check one username."""
    original = input("New username: ")
    username = clean(original)
    problem = policy_problem(username)

    if problem == "":
        print(f"Accepted [{username}].")
    else:
        print(f"Rejected [{username}]: {problem}")


if __name__ == "__main__":
    main()
