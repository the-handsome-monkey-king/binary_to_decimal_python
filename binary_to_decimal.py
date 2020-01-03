#!/usr/bin/env python
"""binary_to_decimal.py

Convert a given binary integer to a decimal integer."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def main():
    try:
        binary_string = (str)(sys.argv[1])
        for digit in binary_string:
            if digit not in ["0", "1"]:
                raise ValueError
    except(ValueError, IndexError):
        print("Usage: binary_to_decimal.py [n]")
        print("[n] = a binary integer")
        sys.exit(1)

    decimal = 0
    length = len(binary_string)
    for i in range(0, length):
        digit = (int)(binary_string[i])
        power = (length-1) - i
        decimal += digit * (2**power)
    print(decimal)

if __name__ == "__main__":
    main()
