import sys;
import datetime;
import math;
import fractions
import random
from functools import reduce
from operator import mul

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
	
	
def countDivisors(primefactors):
	counts = list(primefactors.values());
	counts = [c + 1 for c in counts]
	return reduce(mul, counts)


now = datetime.datetime.now()
print ("Starttime - " + str(now))

i = 1;
triangle=0;
while True:
	triangle = triangle + i;
	count = countDivisors(PrimeFactorization(triangle))
	if (count > 500):
		print(triangle);
		break;
	i = i + 1;

now = datetime.datetime.now()
print ("Endtime - " + str(now))

