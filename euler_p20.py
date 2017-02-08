



def fact(n):
	if(n == 0 or n == 1):
		return 1
	else:
		return n * fact(n-1)
		

x = fact(100)
sum = 0L

while(x > 0):
	sum += x%10
	x = x/10
	
print "Answer: {0}".format(sum)