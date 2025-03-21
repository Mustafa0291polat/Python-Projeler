import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_file> <output_file>")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
        sys.exit("Invalid input or output format")

    if input_file.split('.')[-1] != output_file.split('.')[-1]:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    try:
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image (shirt.png) not found")

    input_image = ImageOps.fit(input_image, shirt_image.size)

    input_image.paste(shirt_image, mask=shirt_image)

    input_image.save(output_file)

if __name__ == "__main__":
    main()
