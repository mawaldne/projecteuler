
Fn_1 = 0;
Fn_2 = 1;
Fn = 0;
totalSum = 0;
while (Fn < 4000000):
	Fn = Fn_1 + Fn_2
	if (Fn%2 == 0):
		totalSum = totalSum + Fn;
	Fn_1 = Fn_2;
	Fn_2 = Fn;
	
print(totalSum);
	
	