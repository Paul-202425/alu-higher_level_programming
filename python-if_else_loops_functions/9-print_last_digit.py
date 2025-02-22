#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")

# Example test cases
uppercase("98")
uppercase("98\n")
uppercase("-98\n")
uppercase("0")

