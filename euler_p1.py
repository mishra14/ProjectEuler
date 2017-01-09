x = 1000
res = 0

for i in xrange(x):
	if(i%3 ==0 or i%5 == 0):
		res = res + i

print "Answer: {}".format(res)
