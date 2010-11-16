file = open('problem67.txt')
a = file.readlines()
a.reverse();


row = [int(c) for c in a[0].split(" ")]
del a[0];

for line in a:
	l = [int(c) for c in line.split(" ")]
	
	for i in range(0,len(l)):
		l[i] = max(row[i] + l[i], row[i+1] + l[i]);
	row = l;
	print(row);

	
