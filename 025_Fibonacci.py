#!/usr/bin/env python3
# 2/9/2020
# PROJECT EULER 
# 1000-digit Fibonacci numberL: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = 1;
b = 1;
index = 2
length = 0

while length <= 3:
	index += 1
	c = a + b 
	a = b
	b = c
	cString = str(c)
	if len(cString) == 1000:
		print(index)
		break