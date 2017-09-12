#!/usr/bin/env python3

import sys
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    # S = input()
    # w = int(input())
    S = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    w = 4
    print(wrap(S, w))
