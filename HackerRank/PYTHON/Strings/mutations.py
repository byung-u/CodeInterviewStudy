#!/usr/bin/env python3

import sys
from functools import reduce

def mutate_string(string, position, character):
    S = list(string)
    S[position] = character
    return (reduce(lambda x, y: x + y, S))


if __name__ == '__main__':
    s = input()
    opt = input().split()
    print(mutate_string(s, int(opt[0]), opt[1]))

