#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 303

For a positive integer n, define f(n) as the least positive multiple of n that, written in base 10, uses only digits ≤ 2.
Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.
Also, . n = 1 ~ 100, f(n)/n = 11363107

Find . n = 1 ~ 10000, f(n)/n = ?

'''

from itertools import cycle, product
from functools import reduce
'''
mul = [ [1],
        [1, 1, 8],
        [1, 4, 1, 4],
        [4, 3, 3],
        [3, 2, 3, 2],
        [2],
        [2, 3, 2, 3],
        [3, 3, 4],
        [4, 1, 4, 1],
        [8, 1, 1]]


def digit_012_check(n):
    while n != 0:
        d, m = divmod(n, 10)
        if m > 2:
            return False
        n = d
    return True


def fn(n):
    if digit_012_check(n):
        print([n], '-', 1, n)
        return 1
    #mul = [ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #        [0, 1, 2],
    #        [0, 1, 5, 6],
    #        [0, 4, 7],
    #        [0, 3, 5, 8],
    #        [0, 2, 4, 6, 8],
    #        [0, 2, 5, 7,],
    #        [0, 3, 6],
    #        [0, 4, 5, 9],
    #        [0, 8, 9]]
    j = 0
    for i in cycle(mul[n % 10]):
        j += i
        m = n * j
        if digit_012_check(m):
            print([n], i, j, m)
            return j
'''


def p303():  # Answer: 1111981904675169, pretty awful though
    L = 10000 + 1
    check = [x for x in range(3, L)]
    result = [0] * L
    result[0] = 1
    result[1] = 1
    result[2] = 2
    # run and check only 9990
    # Found 111333555778 * 9990 = 1112222222222220
    result[9990] = 1112222222222220
    # by hand
    # 9990 answer -> 111333555778
    #  attach [1] -> 1111333555778
    #  attach [3] -> 11113333555778
    #  attach [5] -> 111133335555778
    #  attach [7] -> 1111333355557778
    #  found      -> 1111333355557778
    result[9999] = 11112222222222222222
    check.remove(9990)
    check.remove(9999)
    for i in product([0, 1, 2], repeat=30):
        n = int(reduce(lambda x, y: str(x) + str(y), i))
        temp = []
        for c in check:
            if n % c == 0:
                if n == 0:
                    break
                result[c] = n
                temp.append(c)
                # print([n], c, len(check), check)
        for t in temp:
            check.remove(t)
        if 0 not in result:
            break
    total = 0
    for i in range(1, len(result)):
        # print([i], result[i])
        total += result[i] // i
    print(total)


p303()
