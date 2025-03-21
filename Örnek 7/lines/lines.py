import sys

def count_code_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    code_lines = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped and not stripped.startswith("#"):
            code_lines += 1

    return code_lines

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    print(count_code_lines(filename))

if __name__ == "__main__":
    main()
