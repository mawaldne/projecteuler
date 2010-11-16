import math

l = {}
for a in range(1,1001):
	for b in range(1,1001):
		c = int(math.sqrt(a**2 + b**2))
		if (a**2 + b**2 == c**2 and a+b+c <= 1000):
			if (not(a+b+c in l)):
				l[a+b+c] = 0;
			l[a+b+c] += 1;

max = 0;
maxkey = 0;
for i in l.keys():
	if l[i] > max:
		maxkey = i;
		max = l[i]
	
			
print(maxkey, l[maxkey]/2)