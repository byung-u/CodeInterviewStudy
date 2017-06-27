#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bs4 import BeautifulSoup
from requests import get, codes


def match_soup_class(target, mode='class'):
    def do_match(tag):
        classes = tag.get(mode, [])
        return all(c in classes for c in target)
    return do_match


def main():
    if len(sys.argv) == 1:
        p = 1
    else:
        p = int(sys.argv[1])

    url = 'https://projecteuler.net/problem=%d' % p
    r = get(url)
    if r.status_code != codes.ok:
        print('[url request failed] ', url)
        return
    soup = BeautifulSoup(r.text, 'html.parser')
    for content in soup.find_all(match_soup_class(['problem_content'])):
        print(content.text)


if __name__ == '__main__':
    main()
