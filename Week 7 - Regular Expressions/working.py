import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    match = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
        s
    )

    if not match:
        raise ValueError

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start = convert_time(start_hour, start_min, start_period)
    end = convert_time(end_hour, end_min, end_period)

    return f"{start} to {end}"


def convert_time(hour, minute, period):

    hour = int(hour)

    if minute is None:
        minute = 0
    else:
        minute = int(minute)

    if hour < 1 or hour > 12:
        raise ValueError

    if minute < 0 or minute > 59:
        raise ValueError

    if period == "AM":

        if hour == 12:
            hour = 0

    else:

        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
