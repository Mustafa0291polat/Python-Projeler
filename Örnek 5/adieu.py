def farewell(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

def main():
    names = []
    for _ in range(10):
        try:
            name = input("Name: ")
            if name:
                names.append(name)
        except EOFError:
            break
    print(farewell(names))

main()

