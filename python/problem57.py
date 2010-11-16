from fractions import Fraction 

def root2contfrac(x):
	a = Fraction(1,2)
	while x > 0:
			a = 2 + a
			a = Fraction(1,a)
			x -= 1
	return a + 1
	
total = 0	
for i in range(0,1000):
	x = root2contfrac(i)
	if len(str(x.numerator)) > len(str(x.denominator)):
		total += 1
	print(i, total)
print(total)


