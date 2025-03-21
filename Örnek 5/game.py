import random
import sys

def main():
    while True:
        try:
            level = int(input("level : "))
            if level > 0:
                break

        except ValueError:
            pass

    sayi = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            elif guess < sayi:
                print("Too small!")
            elif guess > sayi:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit(0)
        except ValueError:
            pass
main()
