a = 50
while True:
    if a>=0:
        print(f"Amount Due: {a}")

    b = int(input("Insert Coin: "))

    if b in [25,10,5]:
        a-=b

    if a <= 0:
        print(f"Change Owed: {abs(a)}")
        break
