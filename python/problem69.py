#http://en.wikipedia.org/wiki/Euler's_totient_function
#my shitty slow solution...As per usual. :(

import euler
import datetime 

primefactormap = {}

def primefactorizationset(n, primelist):
	primefactors = set();
	i = 0
	a = primelist[0]
	curr = n
	while (curr > 1):
		if curr in primefactormap:
			primefactors = primefactors.union(primefactormap[curr])
			curr = 0
		elif (curr % a == 0):
			primefactors.add(a)
			curr = curr / a
			i = 0
		else:
			i+=1
		a = primelist[i]

	if (n not in primefactormap):
		primefactormap[n] = primefactors;
	
	return primefactors;

#create prime list
primes = euler.primesieve(1000001)
primelist = []
for i in range(0,len(primes)):
	if primes[i]:
		primelist.append(i)

now = datetime.datetime.now()
print ("Starttime - " + str(now))

max_pn = 0
max_n = 0
n_pn = 0

for n in range(2,1000001):
	if (n % 10000 == 0):
		print(n)
	if (primes[n]):
		n_pn = n/(n-1)
	else:
		primefactors = primefactorizationset(n, primelist)
		pn = n;
		for p in primefactors:
			pn = pn * (1 - 1/p)
		n_pn = n/pn

	if n_pn > max_pn:
		max_pn = n_pn
		max_n = n
	
print(max_n, ' ', max_pn)

now = datetime.datetime.now()
print ("Endtime - " + str(now))


	
	