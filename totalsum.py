#!/usr/bin/python3

import sys

num1 = sys.argv[1]
num = float(num1)

def totalsum(num):
	ans = (num * (num+1))/2
	print(round(ans))

totalsum(num)

