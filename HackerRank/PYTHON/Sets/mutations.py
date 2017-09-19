#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    SA = int(input())
    A = set(map(int, input().split()))
    for _ in range(int(input())):
        S = input().split()
        B = set(map(int, input().split()))

        if S[0] == 'intersection_update':
            A.intersection_update(B)
        elif S[0] == 'update':
            A.update(B)
        elif S[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(B)
        elif S[0] == 'difference_update':
            A.difference_update(B)
    print(sum(A))
