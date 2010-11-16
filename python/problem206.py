#my first slow method...

import re
from itertools import count

def checknum(num):
	#1_2_3_4_5_6_7_8_9_0
	if re.match('1\d2\d3\d4\d5\d6\d7\d8\d9\d0', str(num)):
		return True
	else:
		return False

#print(checknum(1020304050607080900));
#print(checknum(1929394959697989990));
		
for i in count(1010101010,10):	
	if (checknum(i**2)):
		print(i)
		break
			
	if (i > 1389026623):
		print('nothing!')
		break

	if i % 100000 == 0: 
		print(i)

		
