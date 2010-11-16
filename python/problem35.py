def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
 
    max = n**0.5+1
    i = 3
 
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

def CircularNumbers(n):
	i = 0
	n = str(n)
	while (i != len(n)):
		if(n[0] != '0'):
			yield int(n)
		i+=1
		n = n[1:len(n)] + n[0:1]

primes = [];
for i in range(2,1000000):
	if isprime(i):
		primes.append(i);

circularprimes = [];
for p in primes:
	circ = [i for i in CircularNumbers(p) if isprime(i)]
	if len(circ) == len(str(p)):
		circularprimes.append(p);
	
print(circularprimes);
print(len(circularprimes));
print(sum(circularprimes));
		