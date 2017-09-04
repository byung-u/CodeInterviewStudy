#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 111
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11,
2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:
1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit,
N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.
So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275.
It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.
In the same way we obtain the following results for 4-digit primes.

Digit, d M(4, d) N(4, d) S(4, d)
0 2 13 67061
1 3 9 22275
2 3 1 2221
3 3 12 46214
4 3 2 8888
5 3 1 5557
6 3 1 6661
7 3 9 57863
8 3 1 8887
9 3 7 48073

For d = 0 to 9, the sum of all S(4, d) is 273700.
Find the sum of all S(10, d).
'''

from util import is_prime_fermat


def check_2_digit(L, c):
    total = 0
    digits = set()
    for i in range(0, L):
        for j in range(0, L):
            n = [c] * L
            for k in range(0, 10):
                for l in range(0, 10):
                    n[i] = k
                    n[j] = l
                    if n[0] == 0:
                        continue
                    num = int(''.join(list(map(str, n))))
                    digits.add(num)
    for d in digits:
        if is_prime_fermat(d):
            total += d
            print([c], d)
    return total


def p111():  # 612407567715  0.2 sec < run time
    total = 0
    L = 10
    check = [0] * 10
    for i in range(0, 10):
        for j in range(0, L):
            n = [i] * L
            for k in range(0, 10):
                n[j] = k
                if n[0] == 0:
                    continue
                num = int(''.join(list(map(str, n))))
                if is_prime_fermat(num):
                    check[i] += 1
                    total += num
                    print([i], num, check[i])
    for i in range(len(check)):
        if 1 > check[i]:
            ret = check_2_digit(L, i)
            total += ret

    print(total)
    return


p111()
