import sys
def prime_sieve(n):
	l = [1] * (n + 1);
	l[0] = l[1] = 0;
	for i in range(2,n+1):
		for j in range(i**2,n + 1,i):
			l[j] = 0
	return l
	
p = prime_sieve(int(sys.argv[1]))
primes = []
for i in range(len(p)):
	if p[i]:
		primes.append(i)

print(primes)
