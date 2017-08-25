#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.
'''

def p206():
    for i in range(1000000000, 2000000000, 10):
        double_i = i * i
        if str(double_i)[::2] == '1234567890':
            print(i)
            return

p206()
