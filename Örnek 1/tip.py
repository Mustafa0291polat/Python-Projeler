def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Başındaki '$' işaretini kaldırıp, stringi float'a çeviriyoruz
    return float(d.replace('$', ''))

def percent_to_float(p):
    # Sondaki '%' işaretini kaldırıp, stringi float'a çevirip yüzdeyi ondalık hale getiriyoruz
    return float(p.replace('%', '')) / 100

main()
