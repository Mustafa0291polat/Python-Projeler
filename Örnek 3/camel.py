CamelCase = input("CamelCase: ")
Snake_Case = ""

for c in CamelCase:
    if c.isupper():
        Snake_Case += "_" + c.lower()
    else:
        Snake_Case += c


print(Snake_Case)
