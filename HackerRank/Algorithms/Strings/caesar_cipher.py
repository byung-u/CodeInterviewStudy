#!/usr/bin/env python3
import sys

n = int(input().strip())
S = input().strip()
k = int(input().strip())
for s in S:
    if ord(s) > 64 and ord(s) < 91:  # A to Z, 65 - 90
        new_s = ord(s) + (k % 26)
        while new_s > 90:
            new_s -= 26
    elif ord(s) > 96 and ord(s) < 123:  # a to z, 97 - 122
        new_s = ord(s) + (k % 26)
        while new_s > 122:
            new_s -= 26
    else:
        new_s = ord(s)
    print(chr(new_s), end="")
print()
