#There is a pattern in the cube from the bottom right diagonal
# 1 9  25 49 81 121 
# . 7  21 43 73 111
# . 5  17 37 65 101
# . 3  13 31 57 91

# For each Row we're just minusing
# . -2 -4 -6 -8 -10 
# So we can find all values for each diagonal using this recurrence

from itertools import count
from euler import isprime

primes = 0
total = 1
space = 2
for i in count(3,2):
	bottomright = i**2
	bottomleft = bottomright - space
	topleft = bottomleft - space
	topright = topleft - space

	space += 2
	total += 4
	
	if isprime(bottomleft): primes+=1
	if isprime(topleft): primes+=1
	if isprime(topright): primes+=1

	if primes / total < 0.1:
		break

print('primes,total=',primes,total)	
print('size=',i)