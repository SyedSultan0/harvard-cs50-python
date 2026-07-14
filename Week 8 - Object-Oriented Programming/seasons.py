from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        ask = input("Date Of Birth: ")
        print(convert(ask))
    except ValueError:
        sys.exit(1)

def convert(ask):
    a = date.today()
    b = date.fromisoformat(ask)

    diff = a - b
    minutes = int(diff.total_seconds() / 60)

    words = p.number_to_words(minutes)
    words = words.replace(" and ", " ")
    words = words.capitalize()

    return f"{words} minutes"

if __name__ == "__main__":
    main()
