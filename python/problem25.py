import sys
import math

#a = ( (1 + math.sqrt(5)) / 2)
#b = ( (1 - math.sqrt(5)) / 2)

#def f(n):
#	return int(((a**n - b**n)/(a-b)))

n = 1;
n1 = 0;
n2 = 1;

while (len(str(n2)) < 1000):
	n1, n2 = n2, n1 + n2
	n += 1;

print(n);
