#!/usr/bin/env python
"""binary_to_decimal.py

Convert a given binary integer to a decimal integer or vice versa."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def binary_to_decimal(n):
    decimal = 0
    length = len(n)
    for i in range(0, length):
        digit = (int)(n[i])
        power = (length-1) - i
        decimal += digit * (2**power)
    print(decimal)

def decimal_to_binary(n):
    loop_flag = True
    binary_digits = []

    while(loop_flag):
        binary_digits.append(n % 2)
        if n in [0, 1]:
            loop_flag = False
        else:
            n = n / 2

    binary_digits.reverse()
    binary = ""
    for digit in binary_digits:
        binary += "{}".format(digit)
    binary = (int)(binary)
    print(binary)

def error_msg():
    print("Usage: binary_to_decimal.py [n] [options]")
    print("[n] = a positive decimal or binary number")
    print("Unless the option is used, this assumes input is binary.")
    print("[options]")
    print("-d = convert deicmal input to binary")
    sys.exit(1)

def main():
    # determine mode
    binary_input = True
    try:
        option = (str)(sys.argv[2])
        if option == "-d":
            binary_input = False
    except(ValueError, IndexError):
        binary_input = True

    if(binary_input):
        try:
            n = (str)(sys.argv[1])

            binary_string = (str)(sys.argv[1])
            for digit in binary_string:
                if digit not in ["0", "1"]:
                    raise ValueError
        except(ValueError, IndexError):
            error_msg()
        binary_to_decimal(n)

    else:
        try:
            n = (int)(sys.argv[1])
            if (n < 0):
                raise ValueError
        except(ValueError, IndexError):
            error_msg()
        decimal_to_binary(n)

if __name__ == "__main__":
    main()
