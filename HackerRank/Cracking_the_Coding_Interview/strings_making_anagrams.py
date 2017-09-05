#!/usr/bin/env python3
import sys

# def is_anagram(s):


def number_needed(a, b):
    cnt = 0
    temp_a = sort_a = sorted(a)
    temp_b = sort_b = sorted(b)
    for num_b in temp_b:
        if num_b in sort_a:
            sort_b.remove(num_b)
    for num_a in temp_a:
        if num_a in sort_b:
            sort_a.remove(num_a)
    print(sort_a, len(sort_a))
    print(sort_b, len(sort_b))
    return


    if len(sort_a) > len(sort_b):
        print('[before]', sort_b)
        for num_a in sort_a:
            if num_a in sort_b:
                sort_b.remove(num_a)
        print('[after]', sort_b)
    else:
        print('[before]', sort_a)
        for num_b in sort_b:
            if num_b not in sort_a:
                sort_b.remove(num_b)
        print('[after]', sort_a)

        for num_a in sort_a:
            if num_a in sort_b:
                sort_a.remove(num_a)
        print('[last]', sort_a)
        print('[last]', sort_b, len(sort_b))
    
    return

a = input().strip()
b = input().strip()

print(number_needed(a, b))
