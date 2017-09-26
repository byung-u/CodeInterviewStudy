#!/usr/bin/env python3
import sys
import re
from itertools import groupby

n = int(input().strip())
genes = input().strip().split(' ')
health = list(map(int, input().strip().split(' ')))
s = int(input().strip())
h = []
for a0 in range(s):
    first,last,d = input().strip().split(' ')
    first,last,d = [int(first),int(last),str(d)]
        

    cnt = 0
    h.append(cnt)            
print(min(h), max(h))


def very_slow2():
    n = int(input().strip())
    genes = input().strip().split(' ')
    health = list(map(int, input().strip().split(' ')))
    s = int(input().strip())
    h = []
    for a0 in range(s):
        first,last,d = input().strip().split(' ')
        first,last,d = [int(first),int(last),str(d)]
        max_g = max([len(g) for g in genes[first:last+1]])
    
        cnt = 0
        for i in range(0, len(d)):
            print(i)
            for j in range(i + 1, len(d) + 1):
                print('\t', j)
                if j - i > max_g:
                    break
                if d[i:j] in genes[first:last+1]:
                    for idx, g in enumerate(genes[first:last+1]):
                        if d[i:j] == g:
                            # print('-->', health[idx + first], g)
                            cnt += health[idx + first]
        h.append(cnt)            
    print(min(h), max(h))
    

def very_slow1():
    n = int(input().strip())
    genes = input().strip().split(' ')
    health = list(map(int, input().strip().split(' ')))
    s = int(input().strip())
    h = []
    for a0 in range(s):
        first,last,d = input().strip().split(' ')
        first,last,d = [int(first),int(last),str(d)]
    
        cnt = 0
        for i in range(0, len(d)):
            for j in range(i + 1, len(d) + 1):
                if d[i:j] in genes[first:last+1]:
                    for idx, g in enumerate(genes[first:last+1]):
                        if d[i:j] == g:
                            # print('-->', health[idx + first], g)
                            cnt += health[idx + first]
        h.append(cnt)            
    print(min(h), max(h))
