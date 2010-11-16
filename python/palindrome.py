import sys

def ispalindrome(n):
	myStr = str(n)
	if myStr == myStr[::-1]:
		return 1
	else:
		return 0
	
print(isPalindrome(str(sys.argv[1])));
