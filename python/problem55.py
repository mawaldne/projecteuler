def isPalindrome(n):
	return n == n[::-1]
	
def isLychrel(l):
	i = 0;
	while (i <= 50):
		l = l + int(str(l)[::-1].lstrip('0'))
		if (isPalindrome(str(l))):
			return False;
		i += 1;
	return True;

lychrel = [];
for i in range(1,10001):
	if isLychrel(i):
		lychrel.append(i);

print(len(lychrel))