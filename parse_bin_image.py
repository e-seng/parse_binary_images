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

if __name__ == "__main__":
    main()
