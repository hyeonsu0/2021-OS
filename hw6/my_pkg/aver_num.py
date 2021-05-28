#!/usr/bin/python
def aver():
	size = int(input('How many number : '))
	i = 0
	sum = 0
	for i in range(size):
	    num = int(input('Input number : '))
	    sum = sum + num
	ans = sum / num
	print('Average :',ans)

