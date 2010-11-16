import sys

def isPalindrome(n):
	if (len(n) % 2 != 0):
		return False;
	
	i = 0;
	while (i < len(n)/2):
		if (n[i] != n[ (len(n) - 1) - i]):
			return False;
		i = i + 1;

	return True;

i = 100;
maxp=0;
maxi=0;
maxj=0;

while (i <= 999):
	j = 100;
	while (j <= 999):
		if (isPalindrome(str(j * i))):
			print (i, j, j*i, sep=" ", end="\n");
			if (j * i > maxp):
				maxp = j * i;
				maxi = i;
				maxj = j;
		j = j + 1;
	i = i + 1;
	
print (maxi,"*",maxj,"=", maxp);

	




	