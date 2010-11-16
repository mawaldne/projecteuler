f = open('problem59.txt');
encryptedmsg = "".join([n for n in f.readlines()]).replace("\n","").split(',')


passwords = []
for i in range(97,123):
	for j in range(97,123):
		for k in range(97,123):
			passwords.append([i,j,k])

msg = ''
winningpass = []

for password in passwords:
	msg = ''
	i = 0
	while i + 3 < len(encryptedmsg):
		msg += chr(int(encryptedmsg[i]) ^ password[0])
		msg += chr(int(encryptedmsg[i+1]) ^ password[1])
		msg += chr(int(encryptedmsg[i+2]) ^ password[2])
		i+=3

	msg += chr(int(encryptedmsg[i]) ^ password[0])
	
	

		
	if ' and ' in msg:
		print(msg)
		print(password)
		print(sum([ord(a) for a in msg]))
		break
	
