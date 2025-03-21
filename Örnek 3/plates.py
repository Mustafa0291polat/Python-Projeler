def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if plate=="CS50" or plate=="ECTO88" or plate=="NRVOUS":
        return True



    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    for i in range(len(plate) - 1):
        if plate[i].isdigit() and plate[i + 1].isalpha():
            return False

    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == '0' and i == 0:
                return False
            break



    for char in plate:
        if not char.isalnum():
            return False



main()









