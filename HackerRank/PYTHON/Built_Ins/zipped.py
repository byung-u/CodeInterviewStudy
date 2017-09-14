#!/usr/bin/env python3

if __name__ == '__main__':
    val = list(map(int, input().split()))
    N, X = val[0], val[1]
    score = []
    for _ in range(X):
        score.append(list(map(float, input().split())))
    for z in zip(*score):
        print(sum(z) / len(z))
