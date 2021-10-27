#!/usr/bin/python3

import sys
import parse_bin_image

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

if __name__ == "__main__":
    main()
