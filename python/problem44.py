from itertools import combinations
from functools import reduce
import operator
from math import fabs

def pent_list(n):
	n = n * 2
	p = [0] * int((n * ((3*n-1)/2))) 
	for i in range(1,n):
		p[int(i * ((3*i-1)/2))] = 1
	return p

list = [(n * ((3*n-1)/2)) for n in range(1,5000)]
pentlist = pent_list(5000)

for pair in combinations(list, 2):
	p = int(sum(pair))
	n = int(fabs(reduce(operator.sub,pair)))
	if (pentlist[p] and pentlist[n]):
		print(p, n, pair)
		break	


