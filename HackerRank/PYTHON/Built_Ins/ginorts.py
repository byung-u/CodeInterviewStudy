#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    S = input()
    print(*sorted(S, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

    print(*sorted(S, key=lambda x:(x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower() , x)), sep='')

    # print(sorted(S, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
    # print(*sorted( S, key=lambda c: (-ord(c))), sep='')
    # print(*sorted( S, key=lambda c: (-ord(c) >> 5)), sep='')
    # print(*sorted( S, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')


'''
    lower = []
    upper = []
    odd = []
    even = []
    for s in S:
        if s.isupper():
            upper.append(s)
        elif s.islower():
            lower.append(s)
        elif s.isdigit():
            if int(s) % 2 == 0:
                even.append(s)
            else:
                odd.append(s)
    result = []
    result.append(''.join(sorted(lower)))
    result.append(''.join(sorted(upper)))
    result.append(''.join(sorted(odd)))
    result.append(''.join(sorted(even)))
    print(''.join(result))
'''
