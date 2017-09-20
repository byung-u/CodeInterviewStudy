#!/usr/bin/env python3


def minion_game(string):
    kevin, stuart = 0, 0
    ls = len(string)
    for i in range(ls):
        if string[i] in 'AEIOU':
            kevin += ls -i
        else:
            stuart += ls -i

    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart < kevin:
        print('Kevin',  kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
