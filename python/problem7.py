# Here is a faster isprime check
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
	
i = 2;	
primes = [];
while True:
	if (isprime(i)):
		primes.append(i);
	
	if (len(primes) == 10001):
		break;
	i = i + 1;

print ("10001 prime is-",primes[10000]);		
	