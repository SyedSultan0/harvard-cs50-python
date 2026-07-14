import sys


c = 0
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
         a = open(sys.argv[1])
         for b in a:
            b = b.strip()
            if b == "":
                continue
            if b.startswith("#"):
                c += 0
            else:
                c +=1
         print(c)
    except FileNotFoundError:
        sys.exit("File does not exist")
