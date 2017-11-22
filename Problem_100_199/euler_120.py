#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 120
Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.
For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
For 3 ≤ a ≤ 1000, find ∑ rmax.

[Solution]
Odd n: 1, 3, 5, 7
2a
2a3 + 6a
2a5 + 20a3 + 10a
2a7 + 42a5 + 70a3 + 14a

Even n: 2, 4, 6, 8
2a2 + 2
2a4 + 12a2 + 2
2a6 + 30a4 + 30a2 + 2
2a8 + 56a6 + 14a4 + 56a2 + 2

the max remainder
    even a would be (a-2)*a and
     odd a would be (a-1)*a
    -> rmax = (a-1)//2 * 2 * a
'''


def p120_nice():
    # https://benpyeh.com/2013/06/23/project-euler-120/
    L = 1000
    print((L * (L + 1) * (2 * L + 1)) // 6 - 5 - (L - 2) * (L + 3) // 2 - (L // 2 - 1) * (L // 2 + 2))


def p120_nice2():
    # https://blog.dreamshire.com/project-euler-120-solution/
    # (a - 1) // 2 * 2 * a
    print(sum((a - 1) // 2 * 2 * a for a in range(3, 1001)))


def p120():
    total = 0
    for a in range(4, 1001):
        rmax = 0
        for n in range(1, a * 2):
            r = ((a - 1) ** n + (a + 1) ** n) % (a * a)
            if rmax < r:
                rmax = r
        print([a, n], rmax)
        total += rmax
    print(total)


# p120()
p120_nice()
p120_nice2()
