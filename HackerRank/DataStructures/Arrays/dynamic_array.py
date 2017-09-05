#!/usr/bin/env python3
from functools import reduce

arr = []
n = input().strip().split(' ')
for arr_i in range(int(n[1])):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
print(n, arr)
