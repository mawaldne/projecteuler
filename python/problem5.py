import sys
import time


def minNum(n):
	if (n < 20):
		return False;

	#only need to check 11-20. If they are divisible, others below 10 will be
	divs = list(range(11,21));

	for a in divs:
		if (n % a != 0):
			return False;

	return True;
	

a = time.time();
i = 20;
while 1:
	if minNum(i):
		print("The winner - ", i);
		break;
	i = i + 20;
b = time.time();
print ("Time in seconds - ", b - a);