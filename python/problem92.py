chainmap={}
def find_chain_end(i):
	while i != 89 and i != 1:
		istr = str(i)
		i = 0
		for j in range(0,len(istr)):
			i += int(istr[j])**2
		if (i in chainmap):
			return chainmap[i]
	return i

count = 0
for i in range(1,10000000):
	chainmap[i] = find_chain_end(i)
	if chainmap[i] == 89:
		count+=1

print(count)

	
