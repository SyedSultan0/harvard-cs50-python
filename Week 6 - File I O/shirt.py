from PIL import Image, ImageOps
import sys
import os


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:

        formats = [".jpg", ".jpeg", ".png"]

        input_file = os.path.splitext(sys.argv[1])
        output_file = os.path.splitext(sys.argv[2])

        if input_file[1].lower() not in formats:
            sys.exit("Invalid input")

        elif output_file[1].lower() not in formats:
            sys.exit("Invalid output")

        elif input_file[1].lower() != output_file[1].lower():
            sys.exit("Input and output have different extensions")

        else:
            edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input, output):

    try:

        shirt = Image.open("shirt.png")

        with Image.open(input) as image:

            cropped = ImageOps.fit(image, shirt.size)

            cropped.paste(shirt, mask=shirt)

            cropped.save(output)

    except FileNotFoundError:
        sys.exit("Input does not exist")


main()
