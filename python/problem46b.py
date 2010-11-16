#cool simple solution...

from euler import isprime 
 
all = set(i for i in range(3,10000,2))
created = set()
primes = set(i for i in range(1,10000) if isprime(i))
for a in primes:
    for b in range(1,100):
        created.add(a + 2*(b**2))
composite = all - primes
lst = list(composite-created)
lst.sort()
print(lst)

