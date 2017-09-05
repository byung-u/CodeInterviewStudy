#!/usr/bin/env python3

import sys


def insert_sort(l):
    for i in range(1, len(l)):
        if type(l[i]) is int:
            len_save = 1
        else:
            len_save = len(l[i])
        save = int(l[i])
        j = i
        while j > 0:
            if type(l[j - 1]) is int:
                len_j = 1
            else:
                len_j = len(l[j - 1])
            if len_j < len_save:
                break
            if int(l[j - 1]) < save:
                break
            l[j] = l[j - 1]
            j -= 1
        l[j] = save
    return l

n = int(input().strip())
unsorted = []
sorted_arr = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
sorted_arr = insert_sort(unsorted)
sorted_arr = insert_sort(unsorted)
for num in sorted_arr:
    print(num)
