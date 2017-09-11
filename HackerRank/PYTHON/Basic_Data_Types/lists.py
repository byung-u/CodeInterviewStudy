#!/usr/bin/env python3

import sys

'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        S = input().split()
        if S[0] == 'insert':
            L.insert(int(S[1]), int(S[2]))
        elif S[0] == 'append':
            L.append(int(S[1]))
        elif S[0] == 'remove':
            L.remove(int(S[1]))
        elif S[0] == 'pop':
            L.pop()
        elif S[0] == 'reverse':
            L = list(reversed(L))
        elif S[0] == 'sort':
            L = sorted(L)
        elif S[0] == 'print':
            print(L)

