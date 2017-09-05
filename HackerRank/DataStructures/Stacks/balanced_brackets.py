#!/usr/bin/env python3

import sys

def isBalanced(s):
    s = list(s)
    while True:
        for i in range(0, len(s) - 1):
            if ((s[i] == '{' and s[i + 1] == '}') or
                (s[i] == '[' and s[i + 1] == ']') or
                (s[i] == '(' and s[i + 1] == ')')):
                s.pop(i)
                s.pop(i)  # i + 1
                break
        else:
            if len(s) == 0:
                return 'YES'
            else:
                return 'NO'
    return 'NO'


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
