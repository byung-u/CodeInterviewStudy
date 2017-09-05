#!/usr/bin/env python3

import sys

def birthdayCakeCandles(n, ar):
    candles = {}
    for a in ar:
        candles[a] = candles.get(a, 0) + 1
    return candles[max(candles, key=candles.get)]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

