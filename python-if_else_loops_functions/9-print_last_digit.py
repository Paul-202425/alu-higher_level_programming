#!/usr/bin/env python3

# Function definition
def print_last_digit(number):
    """Print and return the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

# Test cases
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

