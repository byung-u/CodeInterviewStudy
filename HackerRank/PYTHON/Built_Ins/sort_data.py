#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    k = int(input().strip())

    for i in sorted(arr, key=lambda x:x[k]):
        print(' '.join(list(map(str, i))))
