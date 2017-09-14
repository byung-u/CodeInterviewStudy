#!/usr/bin/env python3
import sys
from collections import Counter, OrderedDict
from itertools import islice


if __name__ == '__main__':
    S = input().strip()
    S = sorted(S)
    cnt = Counter()
    for s in S:
        cnt[s] += 1
    res = OrderedDict(sorted(cnt.items(), key=lambda t: t[0]))
    res = OrderedDict(sorted(res.items(), key=lambda t: t[1], reverse=True))
    for i in islice(res.items(), 0, 3):
        print(i[0], i[1])
