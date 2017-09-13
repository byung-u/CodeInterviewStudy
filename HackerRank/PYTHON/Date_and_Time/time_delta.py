#!/usr/bin/env python3
import sys
from datetime import datetime


def time_delta(t1, t2):
    do1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    do2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff_do = do1 - do2  # 1 day, 0:30:00
    # print(diff_do, type(diff_do))
    return abs((diff_do.days * 3600 * 24) + diff_do.seconds)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)

