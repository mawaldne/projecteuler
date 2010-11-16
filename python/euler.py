#You can check if a number is prime with a boolean check on l[num]
def primesieve(n):
	l = [1] * (n + 1);
	l[0] = l[1] = 0;
	for i in range(2,n+1):
		for j in range(i**2,n + 1,i):
			l[j] = 0
	return l

def primelist(n):
	primes = primesieve(n)
	primelist = []
	for i in range(0,len(primes)):
		if primes[i]:
			primelist.add(i)
	return primelist
	
def primefactorizationmap(n):
	if (n == 1):
		return {1:0};

	primefactors = {};
	a = 2;
	curr = n;
	while (curr > 1):
		if (curr % a == 0 and isprime(a)):
			if (a in primefactors):
				primefactors[a] += 1;
			else:
				primefactors[a] = 1;
			curr = curr / a;
			a = 2;
		else:
			a = a + 1;
	return primefactors;

def primefactorizationlist(n):
	primefactors = [];
	a = 2;
	curr = n;
	while (curr > 1):
		if (curr % a == 0 and isprime(a)):
			primefactors.append(a);
			curr = curr / a;
			a = 2;
		else:
			a = a + 1;
	return primefactors;
	
#note primes has to be bigger than n
def primefactorizationset(n, primes):
	primefactors = set();
	a = 2;
	curr = n;
	while (curr > 1):
		if (curr % a == 0 and (primes[a] or isprime(a))):
			primefactors.add(a);
			curr = curr / a;
			a = 2;
		else:
			a = a + 1;
	return primefactors;
	


def ispalindrome(n):
	nstr = str(n)
	return nstr == nstr[::-1]

def ispandigital(n):
	nstr = str(n)
	return len(nstr) == 9 and set(nstr) == set("123456789")       
	
def isprime(n):
	if n == 2:
		return True
	if n < 2 or n % 2 == 0:
		return False
 
	'''the trial factors need go no further than n**0.5 because, if n is divisible by some number p, 
	then n = p*q and if q were smaller than p, n would have earlier been detected as being 
	divisible by q or a prime factor of q. '''
	max = int(n**0.5) + 1
	i = 3
	while i < max:
		if n % i == 0:
			return False
		i+=2
	return True

	
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return (a*b) / gcd(a, b)

#slow...
def factors(n):
	factors = [];
	a = 2;
	while (a <= int(n / 2)):
		if (n % a == 0):
			factors.append(a);
		a = a + 1;
	
	factors.append(1);
	factors.append(n);
	factors.sort();
	return factors;