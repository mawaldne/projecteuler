from itertools import count
import math

def trinums(start):
	for n in count(start,1):
		yield (n*(n+1))/2
	
def ispen(n):
	n = (math.sqrt(24*n + 1) + 1) / 6
	return n == int(n)
	
def ishex(n):
	n = (math.sqrt(8*n + 1) + 1) / 4
	return n == int(n)

for i in trinums(40755):
	if ispen(i) and ishex(i):
		print(i)
		break
