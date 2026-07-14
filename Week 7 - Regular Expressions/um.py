import re
import sys


def main():
    a = input("Text: ")
    print(count(a))


def count(s):
    match = re.findall(r"\bum\b", s,re.IGNORECASE)
    return len(match)


...

if __name__ == "__main__":
    main()
