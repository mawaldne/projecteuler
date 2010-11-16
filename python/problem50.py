def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

# speed improvements? Write a sieve algorithm?
# Also put common checks in to a lib
conPrime = [[2,1]];
maxPrime = 2;
maxLength = 1;
for i in range(3,5000):
	if isprime(i):
		conPrime = [ [p[0] + i, p[1] + 1] for p in conPrime]
		conPrime.append([i,1]);
		for j in conPrime:
			if isprime(j[0]) and j[1] > maxLength and j[0] <= 1000000:
				maxPrime = j[0];
				maxLength = j[1];

print(maxPrime, maxLength);
		
		


		