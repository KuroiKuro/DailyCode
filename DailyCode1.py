#!/usr/bin/env python3

'''
This script is to solve Daily Coding Problem No 1
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def listIterate(ls, k):
	for i in ls:
		for j in ls:
			if (i == j):
				continue
			else:
				if (i + j == k):
					print("The numbers are: " + str(i) + " " + str(j))
					return True
				else:
					continue
		return False

def bonus(ls, k):
	'''
	Got the idea to minus the number from K from a dev.to article.
	'''
	ls2 = []
	for i in ls:
		if i in ls2:
			return True
		else:
			ls2.append(k - i)
	return False
#Pseudocode

#Get List
print("Welcome to my script.")
# print("Enter a list of numbers")
# ls = [int(x) for x in input("Enter a list of numbers").split()]
exls = [10, 15, 3, 7]
#Get K
# k = input("Enter K")
exk = 9
#Iterate through List
# listIterate(ls, k);
# bol = listIterate(exls, exk);
bol = bonus(exls, exk)
print(bol)