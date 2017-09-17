#!/usr/bin/env python3

import sys
import bisect
from math import sqrt
from itertools import count

def prime_sieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] is True:
            primes.append(i)

    return primes

def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    return pow(n - 2, n - 1, n) == 1

if __name__ == "__main__":
    primes = prime_sieve(10**6)
    for _ in range(int(input())):
        n = int(input())
        i = bisect.bisect(primes, n)
        print(sum(primes[0:i]))
