#From the forums,,,there is actually a recurrence here that I missed...

def expand(n): 
	(num,den) = (1,2) 
	for i in range(1, n): 
		(num,den) = (den,num + 2*den) 
	return (num,den) 

def nth(n): 
	(num,den) = expand(n) 
	return len(str(num+den)) > len(str(den)) 

counter = 0
for n in range(0, 1000): 
	if nth(n+1): 
		counter += 1 


print(counter)