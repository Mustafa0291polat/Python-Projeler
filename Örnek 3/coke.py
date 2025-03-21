A = 0
print("Amount Due: 50")

while A < 50:
    InsertCoin = int(input("Insert Coin: "))

    if InsertCoin in [5, 10, 25]:
        A += InsertCoin
    else:
        print(f"Amount Due: {50-A}")
        continue

    if A < 50:
        AmountDue = 50 - A
        print(f"Amount Due: {AmountDue}")
    elif A == 50:
        print("Change Owed: 0")
        break
    else:
        ChangeOwed = A - 50
        print(f"Change Owed: {ChangeOwed}")
        break










