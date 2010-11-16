import sys

for a in range(1,1001):
	for b in range(1, 1001):
			if ( (a**2 + b**2) == (1000 - a - b)**2):
				print (a,b,1000-a-b,", a*b*c-", a * b * (1000 - a - b))
				sys.exit();

				
#this one is neat
from math import sqrt
[a * b * sqrt(a**2 + b**2) for a in range(1, 500) for b in range(1, 500) if a + b + sqrt(a**2 + b**2) == 1000]