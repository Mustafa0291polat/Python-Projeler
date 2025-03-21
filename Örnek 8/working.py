import re

def convert(s):
    # Zaman formatını kontrol etmek için regex deseni
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    # Grupları ayır
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    # Zamanları 24 saatlik formata dönüştür
    time1 = convert_to_24_hour(int(hour1), minute1, period1)
    time2 = convert_to_24_hour(int(hour2), minute2, period2)

    return f"{time1} to {time2}"

def convert_to_24_hour(hour, minute, period):
    # Dakika kontrolü
    if minute is None:
        minute = "00"
    elif int(minute) >= 60:
        raise ValueError("Invalid minutes")

    # Saat kontrolü
    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")

    # 24 saatlik formata dönüştür
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute}"

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
