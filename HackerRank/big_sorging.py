#!/usr/bin/env python3

import sys

def q_sort(data, left, right):
    l_hold = left
    r_hold = right
    pivot = data[left]

    while (left < right):
        while ((data[right] >= pivot) and (left < right)):
            right = right-1

        if (left != right):
            data[left] = data[right]

        while ((data[left] <= pivot) and (left < right)):
            left = left+1

        if (left != right):
            data[right] = data[left]
            right = right-1

    data[left] = pivot
    pivot = left
    left = l_hold
    right = r_hold

    if (left < pivot):
        q_sort(data, left, pivot-1)
    if (right > pivot):
        q_sort(data, pivot+1, right)


def quick_sort(data, data_len):
    q_sort(data, 0, data_len-1)
    return data

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(int(unsorted_t))

sorted_arr = quick_sort(unsorted, n)
for i in sorted_arr:
    print(i)
