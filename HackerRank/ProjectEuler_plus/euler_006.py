#!/usr/bin/env python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # http://oeis.org/search?q=1%2C9%2C36%2C100%2C225&language=english&go=Search
    square_of_sum = (n ** 2 * (n + 1) ** 2) / 4
    # http://oeis.org/search?q=1%2C5%2C14%2C30%2C55&sort=&language=english&go=Search
    sum_of_squares = (n * (n + 1) * ((2 * n) + 1)) / 6
    print(square_of_sum - sum_of_squares)
