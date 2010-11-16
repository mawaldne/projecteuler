import itertools

'''
Very slow, very brutish...We don't need to check EVERYTHING...1*2345678=9? no, but it works...
'''
def panprod(s):
	for i in range(0,len(s)-2):
		for j in range(i+1,len(s)-1):
			if (int(s[0:i+1]) * int(s[i+1:j+1]) == int(s[j+1:])):
				yield int(s[j+1:])


'''
Slightly more optimal solution. a * bcde = fghij or ab * cde = fghij. 
'''				
def panprod2(s):
	if int(s[0:1]) * int(s[1:5]) == int(s[5:]):
		return int(s[5:])
	elif int(s[0:2]) * int(s[2:5]) == int(s[5:]):
		return int(s[5:])
	else:
		return 0

l = []	
tot = 0;			
for perm in itertools.permutations([1,2,3,4,5,6,7,8,9],9):
	s = "".join([str(c) for c in perm])
	pan = panprod2(s)
	if pan > 0:
		l.append(pan)

print(l)
print(set(l))
print(sum(set(l)))

