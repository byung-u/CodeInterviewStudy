#!/usr/bin/env python3
from math import atan2, pi, degrees

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    rad = atan2(x, y)
    rad = rad % (2 * pi)
    result = '%d°' % (round(degrees(rad)))
    print(result)


