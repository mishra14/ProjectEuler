import sys
import math

def get_triangle_numbers():
	sum = 0
	i = 1
	while(True):
		yield sum + i
		sum = sum + i
		i  = i + 1

def divisors(n):
	count = 0
	for i in xrange(1, int(math.ceil(math.sqrt(n)))+1):
		if(n%i == 0):
			count += 2
		if(i*i == n):
			count -= 1
	return count
			
numbers = get_triangle_numbers()
limit = 500
while(True):
	n = next(numbers)
	if(divisors(n) >= limit):
		print "Answer: {}".format(n)
		sys.exit()