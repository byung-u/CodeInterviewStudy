#!/usr/bin/env python3

import sys
from string import ascii_lowercase

def print_rangoli(size):
    width = size * 4 - 3
    alphabet = (ascii_lowercase[0:size])[::-1]
    res = []
    for i in range(size):
        s = ''
        for a in alphabet[0:i+1]:
            s = '%s-%s' % (s, a)
        temp = s + s[::-1][1:]
        if len(temp) == width + 2:
            temp = temp[1:-1]
            res.append(temp)
        else:
            res.append(temp.center(width, '-'))

    print('\n'.join(res))
    print('\n'.join(list(reversed(res[0:size - 1]))))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
