import prime_numbers

primes = prime_numbers.get_primes(2000000-1)
res = sum(primes)

print "Answer: {}".format(res)
