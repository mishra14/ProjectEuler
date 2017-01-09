x = 101

sum_sqr = 0
sum_of_sqr = 0

for i in xrange(x):
	sum_sqr = sum_sqr + i
	sum_of_sqr = sum_of_sqr + i*i

sum_sqr = sum_sqr * sum_sqr

print "Answer: {}".format(sum_sqr - sum_of_sqr)
