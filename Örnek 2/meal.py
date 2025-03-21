def main():
    time_str = input("What time is it?")
    time_float = convert(time_str)

    if 7 <= time_float <= 8:
        print("Breakfast time")
    elif 12 <= time_float <= 13:
        print("Lunch time")
    elif 18 <= time_float <= 19:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()

