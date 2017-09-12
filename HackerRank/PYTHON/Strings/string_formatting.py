#!/usr/bin/env python3

import sys


def print_formatted(number):
    max_len = len(format(number, 'b'))

    for i in range(1, number + 1):
        d = i
        o = format(i, 'o')
        h = format(i, 'X')
        b = format(i, 'b')
        print('{0: >{width}}'.format(d, width=max_len), '{0: >{width}}'.format(o, width=max_len), '{0: >{width}}'.format(h, width=max_len), '{0: >{width}}'.format(b, width=max_len))
    

if __name__ == '__main__':
    number = int(input())
    print_formatted(number)

