#!/usr/bin/env python3
from functools import reduce

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

arr = reduce(lambda x, y : x + y, arr)
arr_res = []
for i in range(0, 19, 6):
    for j in range(0, 4):
        n = i + j
        arr_res.append(sum(arr[n:n+3] + arr[n+7:n+8] + arr[n+12:n+15]))
print(max(arr_res))
