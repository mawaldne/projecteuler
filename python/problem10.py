import sys
import datetime 

# Here is a faster isprime check
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
	
	
now = datetime.datetime.now()
print ("Starttime - " + str(now))

#Remove all evens except 2. They are not prime
a = list(range(3, int(sys.argv[1]) + 1))[::2];
a.insert(0,2);

print(sum([n for n in a if isprime(n)]));

now = datetime.datetime.now()
print ("Endtime - " + str(now))
	
	
