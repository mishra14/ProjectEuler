import prime_numbers_oop as prime_numbers
import sys

x = 600851475143

primes = prime_numbers.get_primes(int(x/2))

primes.reverse();

for i in primes:
	if(x%i == 0):
		print "Answer: {}".format(i)
		sys.exit()
