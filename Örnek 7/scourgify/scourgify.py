import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, mode="r") as file:
        reader = csv.DictReader(file)
        rows = []

        for row in reader:
            last, first = row["name"].split(", ")
            rows.append({"first": first, "last": last, "house": row["house"]})

    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
