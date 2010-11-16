from functools import reduce
import operator

nlist = []
dlist = []
for n in range(10,99):
	ns = str(n)
	for d in range(10,99):
		ds = str(d)
		if (n % 10 != 0 and d % 10 !=0 and ns[0] != ns[1] and ds[0] != ds[1]):
				n2,d2 = 1,1;
				if ds.find(ns[0]) != -1:
					n2 = int(ns.replace(ns[0],""))
					d2 = int(ds.replace(ns[0],""))
				elif ds.find(ns[1]) != -1: 
					n2 = int(ns.replace(ns[1],""))
					d2 = int(ds.replace(ns[1],""))
				val1 = n/d
				val2 = n2/d2
				if (val2 < 1 and val1 == val2):
					nlist.append(n)
					dlist.append(d)

print(reduce(operator.mul, nlist))
print(reduce(operator.mul, dlist))

		