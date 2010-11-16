from operator import mul
from functools import reduce 

data = open('problem11.input').readlines()

maxnums = [];

#horizontal
for n in data:
	n = n.split(" ");
	nos = [int(c) for c in n];
	maxnum = max([reduce(mul, nos[i:i+4]) for i in range(len(nos)+1-4)])
	maxnums.append(maxnum)

#vertical
rows = 20
a = [[] for j in range(rows)]
for n in data:
	n = n.split(" ");
	nos = [int(c) for c in n];
	for i in range(len(nos)):
		a[i].append(nos[i]);

for nos in a:
	if (len(nos) >= 4):
		maxnum = max([reduce(mul, nos[i:i+4]) for i in range(len(nos)+1-4)])
		maxnums.append(maxnum)

#diagonally right
rows = 19
a = [[] for j in range(rows)]
for n in data:
	n = n.split(" ");
	nos = [int(c) for c in n];
	for i in range(len(nos)):
		if (i == 0):
			a.insert(0, []);
		a[i].append(nos[i]);

for nos in a:
	if (len(nos) >= 4):
		maxnum = max([reduce(mul, nos[i:i+4]) for i in range(len(nos)+1-4)])
		maxnums.append(maxnum)

#diagonally left
rows = 19
a = [[] for j in range(rows)]
for n in data:
	n = n.split(" ");
	nos = [int(c) for c in n];
	nos = nos[::-1]; #reverse each line and do the same
	for i in range(len(nos)):
		if (i == 0):
			a.insert(0, []);
		a[i].append(nos[i]);

for nos in a:
	if (len(nos) >= 4):
		maxnum = max([reduce(mul, nos[i:i+4]) for i in range(len(nos)+1-4)])
		maxnums.append(maxnum)

print(max(maxnums))

