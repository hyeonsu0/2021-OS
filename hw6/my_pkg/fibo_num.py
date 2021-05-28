#!/usr/bin/python
def fibo():
	num = int(input("fibonacci number ? "))
	list = [0 for i in range(num)]
	i = 0
	sum = 0
	for i in range(num):
	    if(i == 0 or i == 1):
	        list[i] = 1
	    else:
	        list[i] = list[i - 2] + list[i - 1]
	print(list)
	print('F',num,'=',list[num - 1])
