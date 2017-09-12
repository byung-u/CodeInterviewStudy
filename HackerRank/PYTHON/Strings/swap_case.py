#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    s = input()
    RES = ""
    for i in range(len(s)):
        if s[i].isupper():
            RES += s[i].lower()
        else:
            RES += s[i].upper()
    print(RES)
