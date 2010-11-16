# Much much faster solution

def pan(n): return len(n)==9 and "123456789".strip(n)==""
 
prod = set()
for i in range(1,10):
	for j in range(1234,9877):
		if pan(str(i)+str(j)+str(i*j)): prod.add(i*j)
 
for i in range(12,99):
	for j in range(123,988):
		if pan(str(i)+str(j)+str(i*j)): prod.add(i*j)
 
print (sum(prod))