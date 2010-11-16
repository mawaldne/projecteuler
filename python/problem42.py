import string 
import math

def isTriangleNum(n):
	i = math.sqrt((8*n) + 1)
	if i == int(i):
		return True;
	return False;

list = "".join([a.replace("\"", "") for a in open("words.txt").readlines()]).split(",")

triwords = 0;
for name in list:
	i = sum([ord(c.upper()) - 64 for c in name])
	if (isTriangleNum(i)):
		triwords+=1

print(triwords)



	