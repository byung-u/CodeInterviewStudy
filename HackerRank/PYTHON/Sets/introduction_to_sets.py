#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    N = int(input())
    array = input().split()
    res = set()
    for a in array:
        res.add(int(a))
    print(sum(res) / float(len(res)))
