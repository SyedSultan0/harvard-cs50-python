import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"',s)

    if matches:
        video = matches.group(1)
        return f"https://youtu.be/{video}"


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
