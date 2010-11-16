import itertools

def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

max = 0
for i in range(9,0,-1):	
	perms = list(itertools.permutations(list(range(1,i+1)), i))
	for n in perms:
		prime = int("".join([str(j) for j in n]))
		if isprime(prime) and prime > max:
			print(prime)
			max = prime

print(max)