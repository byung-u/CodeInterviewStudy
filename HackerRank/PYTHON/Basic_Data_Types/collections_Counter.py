#!/usr/bin/env python3
import sys
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    x =  input().split()
    count_x = Counter(x)
    N = int(input())
    shoe_size = []
    for _ in range(N):
        i =  input().split()
        shoe_size.append(i)
    res = 0
    for s in shoe_size:
        if count_x[s[0]] != 0:
            res += int(s[1])
            count_x[s[0]] -= 1
    print(res)


