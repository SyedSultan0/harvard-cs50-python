import csv
import sys
students = []



if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    last, first = row[0].split(", ")

                    students.append({
                        "first": first,
                        "last": last,
                        "house": row[1] })

            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

                writer.writeheader()

                for student in students:
                    writer.writerow({
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"] })


    except FileNotFoundError:
        sys.exit("File does not exist")


