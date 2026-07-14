cal =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
cal = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        a = input("Date: ")

        if "/" in a:
            x, y, z = a.split("/")
            x = int(x)
            y = int(y)
            z = int(z)

        else:
            parts = a.split(" ")

            if len(parts) != 3:
                raise ValueError

            x, y, z = parts

            if not y.endswith(","):
                raise ValueError

            y = y.replace(",", "")

            if x not in cal:
                raise ValueError

            x = cal.index(x) + 1
            y = int(y)
            z = int(z)

        if not (1 <= x <= 12 and 1 <= y <= 31):
            raise ValueError

        print(f"{z}-{x:02}-{y:02}")
        break

    except:
        pass
