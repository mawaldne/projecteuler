import sys;
import datetime;
import math;
import euler;
	
def PrimeFactorization(n):
	primefactors = [];
	
	a = 2;
	curr = n;
	while (curr > 1):
		if (curr % a == 0 and euler.isprime(a)):
			primefactors.append(a);
			curr = curr / a;
			a = 2;
		else:
			a = a + 1;
	return primefactors;
	
	
	
now = datetime.datetime.now()
print ("Starttime - " + str(now))

print(PrimeFactorization(int(sys.argv[1])));

now = datetime.datetime.now()
print ("Endtime - " + str(now))
