#!/usr/bin/env python3

import sys


if __name__ == '__main__':
    s = input()
    flags = ['False'] * 5
    for i in range(len(s)):
        if 'False' not in flags:
            print('\n'.join(flags))
            break
        if s[i].isalnum():
            flags[0] = 'True'
        if s[i].isalpha():
            flags[1] = 'True'
        if s[i].isdigit():
            flags[2] = 'True'
        if s[i].islower():
            flags[3] = 'True'
        if s[i].isupper():
            flags[4] = 'True'
    else:
        print('\n'.join(flags))
