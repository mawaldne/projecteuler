
for x in range(100001,200001):
	x2=list(str(2 * x))
	x2.sort()
	x3=list(str(3 * x))
	x3.sort()
	x4=list(str(4 * x))
	x4.sort()
	x5=list(str(5 * x))
	x5.sort()
	x6=list(str(6 * x))
	x6.sort()
	if x2 == x3 == x4 == x5 == x6:
		print(x)
		break

print("done");