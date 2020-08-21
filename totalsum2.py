#!/usr/bin/python3
import sys

num1 = sys.argv[1]
num = int(num1)

s = 0
for i in range(1,(num+1),1):
	s += i

print(s)
