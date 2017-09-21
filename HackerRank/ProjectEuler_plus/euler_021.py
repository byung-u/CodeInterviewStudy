#!/usr/bin/env python3
from math import sqrt

def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n / i))
    return sum(results)

amicables = [220, 1184, 2620, 5020, 6232, 10744, 12285, 17296, 63020, 66928, 67095, 69615, 79750]
temp = []
for a in amicables:
    temp.append(factors(a) - a)

amicables.extend(temp)
amicables = sorted(amicables)

for T in range(int(input())):
    N = int(input())
    print(sum([a for a in amicables if a <= N]))
