#!/usr/bin/env python3
import sys

def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s) - 1):
        ds = abs(ord(s[i]) - ord(s[i-1]))
        dr = abs(ord(r[i]) - ord(r[i-1]))
        if ds != dr:
            return ('Not Funny')
        # print(s[i], s[i-1], r[i], r[i-1])
    return ('Funny')

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)


