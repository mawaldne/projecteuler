#Way better solution from Norvig....

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
	
def PrimeFactorization(n):
	if (n == 1):
		return [1];

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

def divisors(factors):
	ps = sorted(set(factors))
	omega = len(ps)
	def rec_gen(n = 0):
		if n == omega:
			yield 1
		else:
			pows = [1]
			for j in range(factors.count(ps[n])):
				pows += [pows[-1] * ps[n]]
			for q in rec_gen(n + 1):
				for p in pows:
					yield p * q

	for p in rec_gen():
		yield p

	
def d(n):
	return sum(list(divisors(PrimeFactorization(n)))) - n
	
def abundantsum(i): 
	return any(i-a in abundants for a in abundants) 

abundants = set(i for i in range(1,28124) if d(i) > i) 
print(sum(i for i in range(1,28124) if not abundantsum(i)))