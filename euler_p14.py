
x = 1000000

max_count = 0L
max_number = 0

for i in xrange(1, x):
	if(i%10000 == 0):
		print i
	n = i
	count = 0L
	while(n != 1):
		if(n%2 == 0):
			n = n/2
		else:
			n = 3*n + 1
		count += 1
		if(count > max_count):
			max_count = count
			max_number = i

print "Answer: {0} with count {1}".format(max_number, max_count)