def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    digits_started = False
    for char in s:
        if char.isdigit():
            if not digits_started and char == '0':
                return False

            digits_started = True
            
        elif digits_started:
            return False

    return True

if __name__ == "__main__":
    main()
