import itertools

func = itertools.permutations('0123456789',10)
for i in range (1,1000000):
	next(func)

print(reduce(next(func)))

2783915460