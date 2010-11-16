import sys;
import datetime;
import math;
	
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

	
now = datetime.datetime.now()
print ("Starttime - " + str(now))

print(factors(10000));

now = datetime.datetime.now()
print ("Endtime - " + str(now))
