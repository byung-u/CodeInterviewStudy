#!/usr/bin/env python3
if __name__ == '__main__':
    S = input()
    n = 'a'
    cnt = 1
    l = []
    for s in S:
        if n != s:
            if n != 'a':
                # print(n, cnt)
                l.append((cnt, int(n)))
            n = s
            cnt = 1
        else:
            cnt += 1
    # print(s, cnt)
    l.append((cnt, int(s)))
    for r in l:
        print(r, end=" ")
    print()
