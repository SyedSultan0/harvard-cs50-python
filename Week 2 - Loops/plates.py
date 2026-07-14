def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    numberstarted = False
    for ch in s:
        if ch.isdigit():
            if not numberstarted:
                if ch == "0":
                    return False
                numberstarted = True
        else:
            if numberstarted:
                return False

    return True


main()
