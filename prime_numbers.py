

def get_primes(n):
	return sieve_eratosthenes(n)

def sieve_eratosthenes(n):
	sieve = [True for x in xrange(n+1)] # each integer is first marked as non prime
	sieve[0] = False
	sieve[1] = False
	for i in xrange(2, int(n ** 0.5)+1):
		if(sieve[i]):
			done = True
			j = 2
			k = i*j
			while(k < n+1):
				if(sieve[k]):
					sieve[i*j] = False
					done = False
				j = j+1
				k = i*j
		if(done):
			break
	return [x for x in xrange(n+1) if sieve[x]]
	
	
if __name__ == '__main__':
	print get_primes(30)