from itertools import count

def isprime(n):
    if n == 2:
        return True
    if n < 0 or n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True
	
def gen(a,b):
	n = 0;
	while(1):
		p = n**2 + a*n + b
		if (p > 1 and isprime(p)):
			n+=1;
			yield p
		else:
			break
	
maxlen = 0;
maxa=0;
maxb=0;
for a in range(-1000,1001):
	for b in range(-1000,1001):
		count = len(list(gen(a,b)))
		if count > maxlen:
			maxlen = count;
			maxa = a;
			maxb = b;

print (maxlen,maxa,maxb) 



