import re

def count(s):
   
    um_count = len(re.findall(r'\bum\b', s, flags=re.IGNORECASE))
    return um_count

def main():
    text = input("Text: ")
    print(count(text))

if __name__ == "__main__":
    main()
