#!/usr/bin/python3

from PIL import Image
import sys
import os

def main():
    # usage: ./parse_bin_image /path/to/image [OPTIONS]
    filepath = sys.args[1]
    if(not os.path.exists(filepath)):
        print(f"{filepath} not found.\n usage: ./parse_bin_image /path/to/image [OPTIONS]")

def parse_binary_image(filepath, pixel_size=1):
    image = Image.open(filepath)
    pixel_array = image.load()

    width, height = image.size

    # the part where i wish python has regular for syntax :/
    max_x = width // pixel_size
    max_y = heigth // pixel_size

    for(j in range(max_y)):
        y = j * pixel_size
        for(i in range(max_x):
                x = i * pixel_size # jump by the pixel_size to the next pixel
                print(pixel_array[x, y])

if __name__ == "__main__":
    main()
