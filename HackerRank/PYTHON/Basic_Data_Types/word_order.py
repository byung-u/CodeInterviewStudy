#!/usr/bin/env python3

import sys
from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    d = OrderedDict()
    for _ in range(N):
        text = input()
        d[text] = d.get(text, 0) + 1
    print(len(d))
    for val, key in d.items():
        print(key, end=' ')
    print()
