#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    d = {}
    A = int(input())
    room_numbers = list(map(int, input().split()))
    for r in room_numbers:
        d[r] = d.get(r, 0) + 1
    for k, v in d.items():
        if v != A:
            print(k)
