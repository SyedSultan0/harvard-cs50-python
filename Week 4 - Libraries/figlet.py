import pyfiglet
import sys
import random
from pyfiglet import FigletFont

fonts = FigletFont.getFonts()
r = random.choice(fonts)

if len(sys.argv) == 1:
    a = input("Input:")
    f = pyfiglet.figlet_format(a, font=r)
    print(f)

elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    if sys.argv[2] in FigletFont.getFonts():
        a = input("Input:")
        t = pyfiglet.figlet_format(a, font=sys.argv[2])
        print(t)
    else:
        sys.exit(1)

else:
    sys.exit(1)
