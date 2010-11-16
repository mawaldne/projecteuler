import sys;
import datetime;
import math;
import random;
	
def factors(n):
	factors = [];
	a = 2;
	while (a <= int(n / 2)):
		if (n % a == 0):
			factors.append(a);
		a = a + 1;
	
	factors.append(1);
	return factors;

	
now = datetime.datetime.now()
print ("Starttime - " + str(now))

sums = 0;
count = 0;
nums = list(range(0,10001))
for i in nums:
	am1 = sum(factors(i));
	am2 = sum(factors(am1));
	if (i == am2 and i != am1):
		count += 1;
		sums += i + am1;
		nums.remove(am1);
		print(i,am1,am2)

print(sums, count);
now = datetime.datetime.now()
print ("Endtime - " + str(now))