from random import randint


def main():

    a = get_level()

    b = 0
    c = 0

    while b < 10:

        d = 0

        x = generate_integer(a)
        y = generate_integer(a)

        while True:
            try:
                z = int(input(f"{x} + {y} = "))

                if z == x + y:
                    c += 1
                    b += 1
                    break

                else:
                    print("EEE")
                    d += 1

                    if d == 3:
                        print(f"{x} + {y} = {x + y}")
                        b += 1
                        break

            except ValueError:
                print("EEE")
                d += 1

                if d == 3:
                    print(f"{x} + {y} = {x + y}")
                    b += 1
                    break

    print("Score:", c)


def get_level():

    while True:
        try:
            a = int(input("Level: "))

            if a == 1 or a == 2 or a == 3:
                return a

        except ValueError:
            pass


def generate_integer(a):

    if a == 1:
        return randint(0, 9)

    elif a == 2:
        return randint(10, 99)

    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()
