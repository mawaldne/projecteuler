#Can't take credit for this
# http://math.stackexchange.com/questions/8308/working-with-large-exponents
import math

o = open('base_exp.txt')
numlist = o.readlines()

num0 = numlist[0].split(",")
a,b = int(num0[0]),int(num0[1]);
max = b * math.log(a)
pos = 1

for i in range(1,len(numlist)):
	num1 = numlist[i].split(",")
	a,b = int(num1[0]),int(num1[1]);
	if (b * math.log(a)) > max:
		max = (b * math.log(a))
		pos = i + 1
	
print(pos)
	
