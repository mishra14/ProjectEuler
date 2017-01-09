def gcd(a, b):
	while b != 0:
		t = b; 
		b = a % b; 
		a = t;
	return a;

def lcm(a, b):
	return a*b / gcd(a,b)

if __name__ == '__main__':
	x = lcm(1, 2)
	for i in xrange(3, 21):
		res = lcm(x, i)
		x = res

print "Answer: {}".format(res)
