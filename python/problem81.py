data = open('problem81.input').readlines()

m = []
for line in data:
	numstr = line.split(",");
	nums = [int(c) for c in numstr]
	m.append(nums)

maxy = len(m)-1
maxx = len(m)-1	

#update corners
for i in range(maxx-1,-1,-1):
	m[i][maxy] += m[i + 1][maxy]
	m[maxx][i] += m[maxx][i + 1]	

for x in range(maxx-1,-1,-1):
	for y in range(maxy-1,-1,-1):
		if m[x][y] + m[x + 1][y] < m[x][y] + m[x][y + 1]:
			m[x][y] += m[x + 1][y]
		else:
			m[x][y] += m[x][y + 1]

print(m[0][0])			
