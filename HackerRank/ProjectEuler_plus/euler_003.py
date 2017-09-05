#!/usr/bin/env python3

import sys


def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    return pow(n - 2, n - 1, n) == 1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if is_prime(n):
        print(n)
    else:
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if is_prime(n):
                    print(n)
                    break
