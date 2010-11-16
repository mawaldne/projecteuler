from itertools import permutations
perms = list(permutations(list(range(0,10)),10))
total = [];
for n in perms:
	p = "".join([str(j) for j in n]) 
	prime = True 
	if int(p[1:4]) % 2 != 0:
		prime = False
	if int(p[2:5]) % 3 != 0:
		prime = False
	if int(p[3:6]) % 5 != 0:
		prime = False
	if int(p[4:7]) % 7 != 0:
		prime = False
	if int(p[5:8]) % 11 != 0:
		prime = False
	if int(p[6:9]) % 13 != 0:
		prime = False
	if int(p[7:]) % 17 != 0:
		prime = False
	if prime:
		total.append(int(p))

print(sum(total))

