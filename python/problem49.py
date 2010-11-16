from euler import prime_sieve

primes = prime_sieve(10000)

def isperm(i,j):
	return set(str(i)) == set(str(j))			

def isprime(i):
	return primes[i] and primes[i+3330] and primes[i+6660]

perms = []
for i in range(1001,3339,2):
	if isprime(i) and isperm(i,i+3330) and isperm(i+3330,i+6660) and isperm(i,i+6660):
		perms.append((i,i+3330,i+6660))
print(perms)
