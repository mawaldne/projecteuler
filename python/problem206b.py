#Faster and nicer looking, can we do better?

for i in range(101010100, 138902663, 10):
	if str((i + 3) ** 2)[::2] == '123456789': print (i + 3, (i + 3) ** 2)
	if str((i + 7) ** 2)[::2] == '123456789': print (i + 7, (i + 7) ** 2)
	
