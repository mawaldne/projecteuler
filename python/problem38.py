from euler import ispandigital

for i in range(1,10000):
	s=str(i)
	j = 2
	while len(s) < 9:
		s += str(j * int(i))	
		j+=1		
	if (ispandigital(int(s))):
		print(i, s)



	
