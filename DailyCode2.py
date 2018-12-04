#!/usr/bin/env python3
'''
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

from functools import reduce

def listIterate(ls):
	totalProduct = reduce((lambda x, y: x * y), ls)
	# for i in ls:
	# 	totalProduct *= i
	print(totalProduct)
	ls2 = []
	for i in ls:
		ls2.append(int(totalProduct / i))
	return ls2

def listIterateWithoutDivide(ls):
	ls2 = []
	lsLength = len(ls)
	for i in range(0, lsLength):
		number = 1
		for j in range(0, lsLength):
			if (i == j):
				continue
			else:
				number *= ls[j]
		ls2.append(number)
	return ls2

exls = [3,2,1]
exls2 = [1, 2, 3, 4, 5]
ls2 = listIterate(exls2)
ls3 = listIterateWithoutDivide(exls2)
print(ls3)
