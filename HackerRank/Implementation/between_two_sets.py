#!/usr/bin/env python3
from functools import reduce
from math import sqrt


def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def get_lcm_for(set_a):
    return reduce(lambda x, y: lcm(x, y), set_a)


def get_gcd_for(set_a):
    return reduce(lambda x, y: gcd(x, y), set_a)


def getTotalX(a, b):
    if max(a) > min(b):
        return 0
    if len(a) == 1 and a[0] == 1:
        cnt = 0
        for num in range(1, max(b) + 1):
            for num_b in b:
                if num_b % num != 0:
                    break
            else:
                cnt += 1
        return cnt
    lcm_a = get_lcm_for(a)
    # gcd_a = get_gcd_for(a)
    check_x = lcm_a
    cnt = 0
    while check_x < max(b):
        # print( len(b) , len([num for num in b if num % check_x == 0]), check_x)
        if len(b) == len([num for num in b if num % check_x == 0]):
            cnt += 1
        check_x += lcm_a
    return cnt


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)

