def main():
    clock = input("Whats time is it?: ")
    t = convert(clock)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)

    return h + m / 60


if __name__ == "__main__":
    main()
