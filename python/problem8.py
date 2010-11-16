import datetime;
from functools import reduce

def prod(seq):
	def mult(x,y): return int(x)*int(y)
	return reduce(mult, seq)

now = datetime.datetime.now()
print ("Starttime - " + str(now))
	
o = open("problem8.input");
strings = [n for n in o.readlines()];
o.close();	
a = "".join(strings).replace("\n","")

max = prod(a[0:5]);
maxlist = a[0:5];
a = a[1:len(a)];

while (len(a) > 5):
	curr = prod(a[0:5]);
	if (curr > max):
		max = curr;
		maxlist = a[0:5];
	a = a[1:len(a)];
	
print("max is=", max, "with list=", maxlist);

now = datetime.datetime.now()
print ("Endtime - " + str(now))
