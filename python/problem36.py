def isPalindrome(n):
	return n == n[::-1]
	
list = [num for num in range(1,1000001) if (isPalindrome(str(num)) and isPalindrome(bin(num)[2:]))]

print(sum(list))