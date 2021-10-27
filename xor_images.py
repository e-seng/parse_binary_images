#!/usr/bin/python3

import sys
import parse_bin_image
from PIL import Image

def main():
    # usage ./xor_images.py /path/to/image1 /path/to/image2 [OPTIONS]
    fp1 = sys.argv[1]
    fp2 = sys.argv[2]

    pixel_size = "1"

    for arg in sys.argv:
        if "--pixel_size" in arg:
            pixel_size = arg.split("=")[-1]
            continue

    ps = int(pixel_size)
    image1 = parse_bin_image.parse_binary_image(fp1, pixel_size=ps);
    image2 = parse_bin_image.parse_binary_image(fp2, pixel_size=ps);

    min_length = min(len(image1), len(image2))

    xor_out = []

    for i in range(min_length):
        xor_out.append(image1[i] ^ image2[i])

    # get size of the image to enter newlines in appropreate locations
    image = Image.open(fp1);
    width, height = image.size

    row_length = width // ps

    # AGAIN WHY PYTHON MUST YOU BETRAY ME WITH UNCONVENTIONAL FOR SYNTAXES
    for i in range(len(xor_out)):
        insert_char = f"{xor_out[i]}"

        if(i % row_length == 0):
            insert_char += "\n"
        sys.stdout.buffer.write(bytes(insert_char, "utf-8"))

if __name__ == "__main__":
    main()
