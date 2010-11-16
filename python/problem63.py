c = 0
for i in range(1,100):
	for j in range(1,100):
		k = i**j
		if (len(str(k)) == j):
			print(i,j,k)
			c+=1
print("count=" + str(c))
