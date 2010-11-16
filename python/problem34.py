import math 

# done for speed
fac = {};
for i in range(0,10):
	fac[i] = math.factorial(i);

for i in range(1,1000001):
	a = sum([fac[int(n)] for n in list(str(i))])
	if a == i:
		print(i)

	