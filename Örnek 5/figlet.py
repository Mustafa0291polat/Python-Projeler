import sys
import random
from pyfiglet import Figlet

if len(sys.argv) not in [1, 3]:
    print("Invalid usage")
    sys.exit(1)

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        print("Invalid usage")
        sys.exit(1)

    font = sys.argv[2]
    if font not in figlet.getFonts():
        print("Invalid usage")
        sys.exit(1)

    figlet.setFont(font=font)

text = input("Text: ")

print(figlet.renderText(text))



