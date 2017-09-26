#!/usr/bin/env python3
import sys

def theLoveLetterMystery(s):
    r = s[::-1]
    if s == r:
        return 0
    return sum([abs(ord(s[i]) - ord(r[i])) for i in range(0, len(s) // 2)])
    # total = 0
    # for i in range(0, len(s) // 2):
    #     total += abs(ord(s[i]) - ord(r[i]))
    # return total

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)

