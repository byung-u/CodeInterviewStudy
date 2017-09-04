import operator

from collections import defaultdict, deque
from decimal import localcontext, Context, Inexact
from functools import reduce
from math import sqrt, ceil, log10


# Sample
# --------------------------
# return sum(1 for x in range(n+1,  n * 2+1) if ((n * x) % (x - n) == 0))
# ------ use above style ---
# cnt = 0
# for x in range(n+1,  n * 2+1)
#   if ((n * x) % (x - n) == 0)
#       cnt += 1
# print(cnt)
# --------------------------
def matmult(X, Y):
    result = [[0, 0], [0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def fib(n):
    M = [[1, 0], [0, 1]]
    for i in range(1, n):
        M = matmult(M, [[1, 1], [1, 0]])
    return M[0][0]


# def fib(n):
#    '''
#    http://oeis.org/A000045
#    http://mathworld.wolfram.com/FibonacciNumber.html
#
#    Fibonacci
#        - if n = 0; 0
#        - if n = 1; 1
#        - if n > 1; Fn-1 + Fn-2
#    '''
#    if n < 2:
#        # if n == 0 return 0
#        # if n == 1 return 1
#        return n
#    return fib(n-2) + fib(n-1)


def is_palindromic(n):
    '''
    https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
        - Using slice
    '''
    return n == n[::-1]


def is_prime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

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


def prime_factors_uniq(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


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
            results.add(int(n / i))
    return results


def factor_sum(n):
    results = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n / i))
    return sum(results) + 1


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


# Yields prime numbers in ascending order from 2 to limit (inclusive).
def prime_generator(limit):
    if limit >= 2:
        yield 2

    # Sieve of Eratosthenes, storing only odd numbers starting at 3
    isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
    sieveend = sqrt(limit)
    for i in range(len(isprime)):
        if isprime[i] == 1:
            p = i * 2 + 3
        yield p
        if i <= sieveend:
            for j in range((p * p - 3) >> 1, len(isprime), p):
                isprime[j] = 0


def triangle_number(n):
    return int((n * (n + 1)) / 2)


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


def is_perfect_square(x):
    # If you want to allow negative squares, then set x = abs(x) instead
    if x < 0:
        return False

    # Create localized, default context so flags and traps unset
    with localcontext(Context()) as ctx:
        # Set a precision sufficient to represent x exactly; `x or 1` avoids
        # math domain error for log10 when x is 0
        ctx.prec = ceil(log10(x or 1)) + 1  # Wrap ceil call in int() on Py2
        # Compute integer square root; don't even store result, just setting flags
        ctx.sqrt(x).to_integral_exact()
        # If previous line couldn't represent square root as exact int, sets Inexact flag
        return not ctx.flags[Inexact]

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


# print('1234567890'[:9])
# print(not '1234567890'[:9].strip('123456789'))
def is_pandigital(n, s=9):
    return len(n) == s and not '1234567890'[:s].strip(n)


def phi(n):
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Proof_of_Euler.27s_product_formula
    pfs = prime_factors_uniq(n)
    p = 1
    for pf in pfs:
        p *= (1 - (1 / pf))
    return int(round(n * p))


def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)


# https://en.wikipedia.org/wiki/Fermat_primality_test#Concept
# https://gist.github.com/bnlucas/5857437
# a ^ (n-1) ≡ 1 (mod n)
# use a is n - 2
def is_prime_fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    return pow(n - 2, n - 1, n) == 1


# https://oeis.org/A120893
# https://oeis.org/A195531
# Hypotenuses of Pythagorean triples
def hyp(x):  # hypotenuses_of_pythagorean
    if x == 0:
        return 1
    if x == 1:
        return 1
    if x == 2:
        return 5
    return 3 * hyp(x - 1) + 3 * hyp(x - 2) - hyp(x - 3)


def digit_sum(n):
    r = 0
    while n != 0:
        r, n = r + n % 10, n // 10
    return r


def rad(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return reduce(lambda x, y: x * y, list(prime_factors_uniq(n)))


def prime_factors_for_sigma(n):
    i = 2
    factors = {}
    while n % 2 == 0:
        n //= 2
        factors[2] = factors.get(2, 0) + 1

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors


'''
Math function part
'''


# https://en.wikipedia.org/wiki/Divisor_function#Properties
def sigma_x(n, x):
    pf = prime_factors_for_sigma(n)
    s = 1
    for p, a in pf.items():
        s *= ((p ** ((a + 1) * x) - 1) / (p ** x - 1))
    return int(s)

# http://nicklib.com/library/algo/
#    p ∣ a  (a divides b)
#    p ∤ a  (a does not divides b)

# 확장 유클리드 호제법을 이용한 부정방적식의 해 구하기
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# ax + by = g = gcd(a, b).


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0  # gcd, x, y


# 일차 합동식
# http://nicklib.com/library/algo/c/congruence_t.html
# a*x ≡ b (mod m)일 때, x의 값을 구함.
def congruence(a, b, m):
    c, d, e, f = a, m, b, 0
    q, r, tmp = 0, c % d, 0
    while r != 0:
        q, c, d, tmp = c // d, d, r, f
        f, e, r = e - (q * f), tmp, c % d
    if b % d != 0:
        return -1
    q = (f // d) % (m // d)
    if q < 0:
        q += m // d
    return q


# https://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method
# a^n ≡ x (mod m) 일 때, n이 매우 큰 경우
# 10^100000000000000 ≡ 1 (mod 9 * primes)
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    # assert (modulus - 1) * (modulus - 1) not overflow base
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
