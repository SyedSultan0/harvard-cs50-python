while True:
    try:
        a = input("Fraction: ")
        x, y = a.split("/")

        if "." in x or "." in y:
            raise ValueError

        x = int(x)
        y = int(y)

        if y == 0 or x < 0 or y < 0 or x > y:
            raise ValueError

        value = x / y

        if value <= 0.01:
            print("E")
        elif value >= 0.99:
            print("F")
        else:
            print(f"{round(value * 100)}%")

        break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
