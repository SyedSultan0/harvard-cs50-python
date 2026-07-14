import validators

def main():
    a = input("What's your email address?").lower().strip()
    if check(a):
        print("Valid")
    else:
        print("Invalid")

def check(s):
    return validators.email(s)

if __name__ == "__main__":
    main()

