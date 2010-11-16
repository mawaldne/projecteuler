
def pandigital(a, b, c):
    s = str(a) + str(b) + str(c)
    if len(s) != 9: return False
    for i in range(1, 10):
        if -1 == s.find(str(i)): return False
    return True
 
res = set()
for a in range(2, 10000):
    for b in range(2, int(10000/a)):
        if pandigital(a, b, a*b):
            res.add(a*b)
print(sum(res))