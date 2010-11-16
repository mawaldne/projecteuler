#my typical slow first solution...
from euler import prime_sieve 

primes = prime_sieve(10000)

def goldbach(p, i):
	return p + 2 * (i ** 2) 

for c in range(9,10000,2):
	if primes[c]:
		continue
	found = False
	for p in range(1,c): 	
		if not primes[p]:
			continue
		for i in range(1,c-1):
			cnew = goldbach(p, i)
			if cnew == c:
				#print(c, "=", p, "+", "2 *", i, "** 2")
				found = True
				break
			if cnew > c:
				break;
		if found:
			break
	if not found:
		print(c);
		break;
