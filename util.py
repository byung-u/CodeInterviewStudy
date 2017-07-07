import operator

from math import sqrt
from functools import reduce


def fib(n):
    '''
    http://oeis.org/A000045
    http://mathworld.wolfram.com/FibonacciNumber.html

    Fibonacci
        - if n = 0; 0
        - if n = 1; 1
        - if n > 1; Fn-1 + Fn-2
    '''
    if n < 2:
        # if n == 0 return 0
        # if n == 1 return 1
        return n
    return fib(n-2) + fib(n-1)


def is_palindromic(n):
    '''
    https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
        - Using slice
    '''
    return n == n[::-1]


def is_prime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    # n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prod(factors):
    return reduce(operator.mul, factors, 1)


def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return results


def is_square(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


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


def triangle_number(n):
    return int((n * (n+1)) / 2)


def pentagonal_number(n):
    return int(n * ((3 * n) - 1) / 2)


def hexagonal_number(n):
    return int(n * (2 * n - 1))


def is_triangle(n):
    # https://en.wikipedia.org/wiki/Triangular_number
    t = (sqrt((8 * n) + 1) - 1) / 4
    return t.is_integer()


def is_square(n):
    s = sqrt(n)
    return s.is_integer()


def is_pentagonal(n):
    # https://stackoverflow.com/questions/37390233/python-is-pentagonal-number-check
    # https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
    p = (sqrt((24 * n) + 1) + 1) / 6
    return p.is_integer()


def is_hexagonal(n):
    # https://en.wikipedia.org/wiki/Hexagonal_number
    h = (sqrt((8 * n) + 1) + 1) / 4
    return h.is_integer()


def is_heptagonal(n):
    # https://en.wikipedia.org/wiki/Heptagonal_number
    h = (sqrt((40 * n) + 9) + 3) / 10
    return h.is_integer()


def is_octagonal(n):
    # https://en.wikipedia.org/wiki/Octagonal_number
    o = (sqrt((3 * n) + 1) + 1) / 3
    return o.is_integer()
