import math

def ncr(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
	
list = [];
for n in range(2, 101):
	for r in range(2, n):
		val = ncr(n,r)
		if (val > 1000000):
			list.append(val);

print(len(list))
		