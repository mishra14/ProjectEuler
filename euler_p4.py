x = 999
y = 100
res = -1

for i in xrange(x, y, -1):
	for j in xrange(x, y, -1):
		z = i*j
		s = str(z)
		if(s == s[::-1] and z > res):
			res = z

print "Answer: {}".format(res)
