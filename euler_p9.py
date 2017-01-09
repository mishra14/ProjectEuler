import sys

x = 999

for a in xrange(1, x):
	for b in xrange(1, x):
		for c in xrange(1, x):
			if(a+b+c == 1000 and a*a + b*b == c*c):
				print "a, b, c: {}, {}, {}".format(a, b, c)
				print "Answer: {}".format(a*b*c)
				sys.exit()