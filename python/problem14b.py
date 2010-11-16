# Mine was pretty slow..Heres something faster. Why is this faster?
# Saves all previous answers in a hashmap!
# For example, look at Collatz(13)...The iteration goes 13->40->20->10->5->16->8->4->2->1. So we know 13 has a
# 10 steps, then that means 40 is going to have 9 steps, 20 will have 8 steps...Etc...So if we save all theses numbers
# in a map, if we ever hit them again, we won't have to recalculate the number of steps. Just add them to the current 
# step count. Cool
import datetime;

collatz = {1:1} 
def Collatz(n): 
	global collatz 
	if not n in collatz: 
		if n%2 == 0: 
			collatz[n] = Collatz(n/2) + 1 
		else: 
			collatz[n] = Collatz((3*n + 1)/2) + 2 
	return collatz[n] 

now = datetime.datetime.now()
print ("Starttime - " + str(now))

for j in range(1000000,0,-1): 
	Collatz(j)

print(list(collatz.keys())[(list(collatz.values()).index(max(list(collatz.values()))))]);
	
now = datetime.datetime.now()
print ("Endtime - " + str(now))