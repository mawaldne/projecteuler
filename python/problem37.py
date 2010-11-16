from itertools import count

def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True
	
def istrun(n):
	s = str(n)
	for i in range(len(s)):
		if not isprime(int(s[:i+1])) or not isprime(int(s[i:])):
			return False
	return True

tprimes = []; 
for i in count(11,1):
	if isprime(i) and istrun(i): 
		print(i);
		tprimes.append(i);
	if len(tprimes) == 11:
		break;

print(tprimes)
print(sum(tprimes))

	