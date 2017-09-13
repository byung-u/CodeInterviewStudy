#!/usr/bin/env python3
from itertools import product

if __name__ == '__main__':
    x = list(map(int, (input().split())))
    y = list(map(int, (input().split())))
    for n in list(product(x, y)):
        print(n, end=" ")
    print()
