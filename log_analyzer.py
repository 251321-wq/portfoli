"""Analyze authentication log entries."""

ALERT_LIMIT = 3

LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name):
    """Return the value after name= up to the next space or the end."""
    marker = name + "="
    start = line.find(marker)
    if start == -1:
        return ""
    start += len(marker)
    end = line.find(" ", start)
    if end == -1:
        return line[start:]
    return line[start:end]


def get_status(line):
    """Return the second word of a log line."""
    words = line.split()
    if len(words) < 2:
        return ""
    return words[1]


def count_status(status):
    """Return the number of log lines with the requested status."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == status:
            count += 1
    return count


def show_summary():
    """Print the total, failed, and successful log-line counts."""
    lines = LOG.splitlines()
    print(f"Lines: {len(lines)}")
    print(f"Failed: {count_status('FAILED')}")
    print(f"OK: {count_status('OK')}")


def search(keyword):
    """Print numbered log lines containing keyword, then the match count."""
    matches = 0
    for number, line in enumerate(LOG.splitlines(), start=1):
        if keyword.lower() in line.lower():
            print(f"{number}: {line}")
            matches += 1
    print(f"Matches: {matches}")


def ip_report(ip):
    """Print failed-login times and users for an IP, plus an alert if needed."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            print(f"{line.split()[0]} {get_field(line, 'user')}")
            count += 1
    print(f"Failed logins from {ip}: {count}")
    if count >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")


def mask(word):
    """Keep the first and last letters and replace the middle with asterisks."""
    if len(word) <= 2:
        return "*"
    return word[0] + "*" * (len(word) - 2) + word[-1]


def show_masked():
    """Print every log line with each user name masked."""
    for line in LOG.splitlines():
        user = get_field(line, "user")
        if user != "":
            line = line.replace(f"user={user}", f"user={mask(user)}")
        print(line)


def show_menu():
    """Print the analyzer title and its five menu choices."""
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")


def main():
    """Run the interactive authentication-log analyzer."""
    show_menu()
    while True:
        choice = input("Choice: ").strip().lower()
        if choice == "1":
            show_summary()
        elif choice == "2":
            keyword = input("Keyword: ")
            search(keyword)
        elif choice == "3":
            ip = input("IP: ").strip()
            ip_report(ip)
        elif choice == "4":
            show_masked()
        elif choice == "q":
            print("Bye.")
            break
        else:
            print("Unknown choice.")


if __name__ == "__main__":
    main()
