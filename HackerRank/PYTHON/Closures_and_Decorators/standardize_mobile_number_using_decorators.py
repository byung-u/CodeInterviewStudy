#!/usr/bin/env python3

import sys
# +918689745612
# 09687456321

def wrapper(f):
    def fun(l):
        for i, num in enumerate(l):
            if len(l[i]) == 10:
                l[i] = '+91 %s %s' % (l[i][0:5], l[i][5:])
            elif len(l[i]) == 11:
                l[i] = '+91 %s %s' % (l[i][1:6], l[i][6:])
            elif len(l[i]) == 12:
                l[i] = '+91 %s %s' % (l[i][2:7], l[i][7:])
            elif len(l[i]) == 13:
                l[i] = '+91 %s %s' % (l[i][3:8], l[i][8:])
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

