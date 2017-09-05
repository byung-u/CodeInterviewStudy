#!/usr/bin/env python3
import sys

def shift(input_list, n):
    n = n % len(input_list)
    return input_list[n:] + input_list[:n]

def array_left_rotation_slow(a, n, k):
    ret = []
    for i in range(0, k + 1):
        ret = shift(a, i)
    return ret

def array_left_rotation(a, n, k):
    ret = a[k:] + a[0:k]
    return ret

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
