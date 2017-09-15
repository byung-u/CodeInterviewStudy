#!/usr/bin/env python3

from functools import reduce
from itertools import permutations, product, combinations
arr = [1, 2, 3, 4, 5]
n = len(arr)

ret = [reduce(lambda x, y: x + y, i) for i in combinations(arr, n - 1)]
print(min(ret), max(ret))
