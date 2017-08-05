#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json


def match_soup_class(target, mode='class'):
    def do_match(tag):
        classes = tag.get(mode, [])
        return all(c in classes for c in target)
    return do_match


def main():
    if len(sys.argv) != 3:
        print('Problem number, and Answer')
        sys.exit(1)
    else:
        num = int(sys.argv[1])
        if num > 330:
            print('We have just 330 problems solution')
            sys.exit(1)
        ans = int(sys.argv[2])

    js = json.load(open('problems.json'))
    if ans == 0:
        print(js[num-1]['answer'])
        sys.exit(1)

    if ans == int(js[num-1]['answer']):
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    else:
        print('\x1b[0;37;41m' + 'Failed!' + '\x1b[0m')


if __name__ == '__main__':
    main()
