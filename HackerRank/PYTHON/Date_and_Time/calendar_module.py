#!/usr/bin/env python3
from calendar import weekday, day_name

if __name__ == '__main__':
    D = list(map(int, input().split()))
    days = list(day_name)
    day = weekday(D[2], D[0], D[1])
    print(str(days[day]).upper())
