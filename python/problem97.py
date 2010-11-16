'''
n = 1;
for i in range(1,7830458):
	n = n * 2
	s = str(n)
	if (len(s) > 10):
		n = int(s[(len(s)-10):])
	else:
		n = int(s)

n = (28433 * n) + 1
print(n);
'''
#Heres a beter one:
'''
n = 2
for i in range(7830456): n = (n * 2) % 10000000000		
n = n * 28433 + 1
print(str(n)[-10:])
'''

#Even better, and faster
a = 2**7830457
b = int( a% 10000000000 ) # last 10 digits of 2**(...)
c = b * 28433
c = c+1
print(c % 10000000000  ) # last 10 digits
	