#!/usr/bin/env python3

if __name__ == '__main__':
    val = list(map(int, input().split()))
    x, k = val[0], val[1]
    P = input().split()
    res = 0
    flag = '+'
    for i, p in enumerate(P):
        if i % 2 == 1:
            flag = p
        else:
            if p.find('**') != -1:
                e = p.split('**')
                temp = pow(x, int(e[1]))
                if e[0].find('*') != -1:
                    e2 = e[0].split('*')
                    temp *= int(e2[0])
                if flag == '+':
                    res += temp
                elif flag == '-':
                    res -= temp
                elif flag == '*':
                    res *= temp
                elif flag == '/':
                    res //= temp
            elif p.find('x') != -1:
                if flag == '+':
                    res += x
                elif flag == '-':
                    res -= x
                elif flag == '*':
                    res *= x
                elif flag == '/':
                    res //= x
            else:
                if flag == '+':
                    res += int(p)
                elif flag == '-':
                    res -= int(p)
                elif flag == '*':
                    res *= int(p)
                elif flag == '/':
                    res //= int(p)
    if res == k:
        print('True')
    else:
        print('False')
