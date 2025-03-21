import re

def validate(ip):
    # Use regex to match the IPv4 format
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if not match:
        return False

    # Check if each number is between 0 and 255
    for num in match.groups():
        if not (0 <= int(num) <= 255):
            return False

    return True

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

if __name__ == "__main__":
    main()
