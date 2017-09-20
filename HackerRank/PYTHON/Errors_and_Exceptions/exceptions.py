#!/usr/bin/env python3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input().split()
        try:
            a = int(s[0])
        except ValueError as e:
            print("Error Code:", e)
            continue

        try:
            b = int(s[1])
        except ValueError as e:
            print("Error Code:", e)
            continue

        try:
            print(a // b)
        except ZeroDivisionError as e:
            print("Error Code:", e)
