
n = 2 ** 1000
sum = 0L

while(n > 0):
	sum += n%10
	n = n/10
	
print "Answer: {0}".format(sum)