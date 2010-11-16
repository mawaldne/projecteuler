#http://mathworld.wolfram.com/RepeatingDecimal.html
'''
From a bit of research on mathworld, I learned that, for fractions 1/n, the decimal representation only repeats for n that are 
relatively prime to 10 (makes sense). Furthermore, the number of repeating digits is equal to the multiplicative order of 10 modulo n. 
Finally, the maximum number of repeating digits is n-1. 
'''

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return (a*b) / gcd(a, b)
 
def isPrime(p):
    return (p > 1) and all(f == p for f,e in factored(p))
 
primeList = [2,3,5,7]
def primes():
    for p in primeList:
        yield p
    while 1:
        p += 2
        while not isPrime(p):
            p += 2
        primeList.append(p)
        yield p
 
def factored( a):
    for p in primes():
        j = 0
        while a%p == 0:
            a /= p
            j += 1
        if j > 0:
            yield [p,j]
        if a < p*p: break
    if a > 1:
        yield [a,1]
 
 
def multOrdr1(a,p,e):
    m = p**e
    t = (p-1)*(p**(e-1)) #  = Phi(p**e) where p prime
    qs = [1,]
    for f in factored(t):
        qs = [ q * f[0]**j for j in range(1+f[1]) for q in qs ]
    qs.sort()
 
    for q in qs:
        if pow( int(a), int(q), int(m) )==1: break
    return q
 
 
def multOrder(a,m):
    mofs = (multOrdr1(a,r[0],r[1]) for r in factored(m))
    return reduce(lcm, mofs, 1)
 
# 0, 0, 1, 0, 0, 1, 6, 0, 1, 0, 2, 1, 6, 6, 1, 0, 16, 1, 18, 
if __name__ == "__main__":
	max = 0;
	ans = -1;
	for i in range(1,1001):
		if gcd(10,i) == 1:
			x = multOrder(10, i)
			if x > max:
				max = x;
				ans = i;

	print(max, ans);