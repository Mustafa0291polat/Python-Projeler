def main():
    result = get_fuel_percentage()
    print(result)


def get_fuel_percentage():
    while True:
        try:
            fraction = input("Yakıt seviyesini girin (X/Y formatında): ")

            fraction_parts = fraction.split("/")
            x = int(fraction_parts[0])
            y = int(fraction_parts[1])

            if x > y or y == 0:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except (ValueError, ZeroDivisionError):
            print("Geçersiz giriş. Lütfen tekrar deneyin.")

main()


