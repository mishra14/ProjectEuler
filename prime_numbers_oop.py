
class Sieve:
	max_length = 536870912
	
	def __init__(self, n):
		print n
		print Sieve.max_length
		print n/Sieve.max_length
		count = n/Sieve.max_length + 1 if(n % Sieve.max_length > 0) else 0
		print count
		# each integer is first marked as prime
		self.sieve = [[True for i in xrange(Sieve.max_length if j <count -1 else n % Sieve.max_length)] for j in xrange(count)]
		
	def set(self, index, value):
		(i, j) = self.transform_index(index)
		self.sieve[i][j] = value
		
	def get(self, index):
		(i, j) = self.transform_index(index)
		return self.sieve[i][j]
		
	def transform_index(self, index):
		i, j = index/Sieve.max_length, index % Sieve.max_length
		return (i, j)

	def transform_indices(self, i, j):
		index = i*Sieve.max_length + j
		return index
		
	def get_primes(self):
		for i in xrange(len(self.sieve)):
			for j in xrange(len(self.sieve[i])):
				if(self.sieve[i][j]):
					yield self.transform_indices(i, j)
		
def get_primes(n):
	return sieve_eratosthenes(n)

def sieve_eratosthenes(n):
	sieve = Sieve(n+1) # n+1 as n has to be included in the list
	sieve.set(0, False)
	sieve.set(1, False)
	for i in xrange(2, int(n ** 0.5)+1):
		if(sieve.get(i)):
			done = True
			j = 2
			k = i*j
			while(k < n+1):
				if(sieve.get(k)):
					sieve.set(k, False)
					done = False
				j = j+1
				k = i*j
		if(done):
			break
	return sieve.get_primes()
	
	
if __name__ == '__main__':
	print list(get_primes(30))