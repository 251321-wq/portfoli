"""Validate IPv4 addresses."""

def is_valid_part(part):
    """Return True when part contains only decimal digits and is from 0 to 255."""
    return part.isdecimal() and int(part) <= 255


def ip_problem(address):
    """Return the first problem with an IPv4 address, or an empty string."""
    if address.count(".") != 3:
        return "it needs exactly 3 dots."

    for part in address.split("."):
        if part == "":
            return "a part is empty."
        if not is_valid_part(part):
            return f"{part} is not a number from 0 to 255."

    return ""


def main():
    """Read an IPv4 address and report whether it is valid."""
    address = input("IPv4 address: ").strip()
    print(f"IPv4 address: {address}")
    problem = ip_problem(address)

    if problem == "":
        print(f"{address} is valid.")
    else:
        print(f"Invalid: {problem}")


if __name__ == "__main__":
    main()
