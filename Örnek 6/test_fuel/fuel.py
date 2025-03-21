def main():
    fraction = input("Fraction (X/Y): ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        return round((x / y) * 100)
    except ValueError:
        raise ValueError("Invalid input. Fraction must be in X/Y format with integers.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()



