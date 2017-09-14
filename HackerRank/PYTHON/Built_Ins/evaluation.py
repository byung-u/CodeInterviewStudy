#!/usr/bin/env python3

if __name__ == '__main__':
    S = input()
    if S.startswith('print(') == 0:
        print(eval(S))
    else:
        eval(S)
