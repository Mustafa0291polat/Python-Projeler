# outdated.py
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def convert_date(date):
    # Ay-Gün-Yıl formatı için kontrol
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year:04}-{month:02}-{day:02}"
        except ValueError:
            return None

    # Ay adı ile format için kontrol
    elif "," in date:  # Virgül kontrolü ekleniyor
        try:
            month_name, day_year = date.split(" ", 1)
            day, year = day_year.replace(",", "").split()
            day, year = int(day), int(year)
            if month_name in months and 1 <= day <= 31:
                month = months.index(month_name) + 1
                return f"{year:04}-{month:02}-{day:02}"
        except (ValueError, IndexError):
            return None

    return None

while True:
    date_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ")
    iso_date = convert_date(date_input)
    if iso_date:
        print(iso_date)
        break
    else:
        print("Invalid date. Please try again.")

