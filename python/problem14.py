import datetime;

def collatz(n):
	count = 0;
	while (n != 1):
		if (n % 2 == 0):
			count+=1;
			n = int(n / 2);
		else:
			count+=2;
			n = int(((3*n + 1)/2));
	count+=1;
	return count;

max = 0;
i = 1;
answer = i;

now = datetime.datetime.now()
print ("Starttime - " + str(now))

for j in range(1000000,0,-1): 
	count = collatz(j);
	if (count > max):
		max = count;
		answer = j;

	
print(answer);

now = datetime.datetime.now()
print ("Endtime - " + str(now))