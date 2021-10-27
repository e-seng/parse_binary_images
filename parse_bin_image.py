#!/usr/bin/python3

from PIL import Image
import sys
import os

def main():
    # usage: ./parse_bin_image /path/to/image [OPTIONS]
    filepath = sys.argv[1]
    if(not os.path.exists(filepath)):
        print(f"{filepath} not found.\n usage: ./parse_bin_image /path/to/image [OPTIONS]")

    pixel_size = "1"

    for arg in sys.argv:
        if("--pixel_size" in arg):
            pixel_size = arg.split("=")[-1]
            continue

    ps = int(pixel_size)
    print(parse_binary_image(filepath, pixel_size=ps))

def parse_binary_image(filepath, pixel_size=1):
    binary_values = []

    image = Image.open(filepath)
    pixel_array = image.load()

    width, height = image.size

    # the part where i wish python has regular for syntax :/
    max_x = width // pixel_size
    max_y = height // pixel_size

    for j in range(max_y):
        y = j * pixel_size
        for i in range(max_x):
                x = i * pixel_size # jump by the pixel_size to the next pixel
                pixel_value = pixel_array[x, y][0] # only read the R value since it should be back/white

                # 0 for whiter pixels, 1 for blacker pixels (relative to 50% grey)
                bin_value = int(pixel_value > 128)
                binary_values.append(bin_value)

    return binary_values

if __name__ == "__main__":
    main()
