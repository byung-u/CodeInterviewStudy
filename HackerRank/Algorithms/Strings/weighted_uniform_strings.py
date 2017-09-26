#!/usr/bin/env python3
import sys
from itertools import groupby
import string

def slow_work1():
    L = list(string.ascii_lowercase)
    S = list(map(str, input().strip()))
    new_s = []
    last_c = ''
    last_cnt = 0
    # print(S)
    for i in range(0, len(S)):
        if S[i] == last_c:
            new_s.append((L.index(S[i]) + 1) * last_cnt)
            last_cnt += 1
        else:
            new_s.append(L.index(S[i]) + 1)
            last_c = S[i]
            last_cnt = 2
    x = []
    for _ in range(int(input())):
        n = int(input())
        x.append(n)
    # print(new_s, x)
    for n in x:
        if n in new_s:
            print('Yes')
        else:
            print('No')


def slow_work2():
    L = list(string.ascii_lowercase)
    S = list(map(str, input().strip()))
    CS=Counter(S)

    new_s = []
    for k, v in CS.items():
        for i in range(1, v + 1):
            new_s.append((L.index(k) + 1) * i)
    
    for _ in range(int(input())):
        n = int(input())
        if n in new_s:
            print('Yes')
        else:
            print('No')


def bad_count1():
    L = list(string.ascii_lowercase)
    S = list(map(str, input().strip()))
    CS=Counter(S)
    print(CS)
    new_s = []
    for k, v in CS.items():
        for i in range(1, v + 1):
            new_s.append((L.index(k) + 1) * i)
            if((L.index(k) + 1) * i) == 9810:
                print(k, v)
    
    temp = set(new_s)
    
    
    for _ in range(int(input())):
        n = int(input())
        if n in temp:
            print('Yes')
        else:
            print('No')


# Success
L = list(string.ascii_lowercase)
S = input().strip()
CS = sorted([list(g) for k, g in groupby(S)])
new_s = []
for C in CS:
    for i, c in enumerate(C):
        new_s.append((L.index(c) + 1) * (i + 1))

temp = set(new_s)
for _ in range(int(input())):
    n = int(input())
    if n in temp:
        print('Yes')
    else:
        print('No')
