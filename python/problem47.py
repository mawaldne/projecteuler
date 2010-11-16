from euler import primefactorizationmap

p1 = primefactorizationmap(1)
p2 = primefactorizationmap(2)
p3 = primefactorizationmap(3)
p4 = primefactorizationmap(4)
i = 4

while (True):
	if len(p1.keys()) == len(p2.keys()) == len(p3.keys()) == len(p4.keys()) == 4:
		print("done:",i - 3)
		break
	p1 = p2
	p2 = p3
	p3 = p4
	i+=1
	p4 = primefactorizationmap(i)


















