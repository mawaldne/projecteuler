file = open('problem18.txt')
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

	

''' Heres another good solution
triangle = """(paste in triangle here or read an input file)"""
 
triangle = [map(int, line.split(' ')) for line in triangle.split('\n')]
 
for rowi in xrange(len(triangle) - 2, -1, -1):
	for itemi in xrange(len(triangle[rowi])):
		triangle[rowi][itemi] += max((triangle[rowi + 1][itemi], triangle[rowi + 1][itemi + 1]))
 
print triangle[0][0]
'''