import sys
import csv
from tabulate import tabulate

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    # Check if the file is a CSV file
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open and read the file
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Generate and print the ASCII table
    table = tabulate(rows, headers=headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
