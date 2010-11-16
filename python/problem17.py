numToWord = {
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
1000:'onethousand',
'hundred':'hundred',
'and':'and'
}

def countDigit(s):
	if (s == '0'):
		return 0;
	
	if len(s) == 3:
		if (int(s[1]) > 0 or int(s[2]) > 0):
			return len(numToWord[int(s[0])] + numToWord['hundred'] + numToWord['and']) + countDigit(s[1:])
		else:
			return len(numToWord[int(s[0])] + numToWord['hundred']) + countDigit(s[1:])
	
	elif len(s) == 2 and int(s[0]) == 0:
		return 0 + countDigit(s[1:])
	elif len(s) == 2 and int(s[0]) == 1:
		return len(numToWord[int(s)])
	elif len(s) == 2 and int(s[0]) > 1:
		return len(numToWord[ int(s[0]) * 10 ]) + countDigit(s[1:])
	elif len(s) < 2 or len(s) == 4:
		return len(numToWord[int(s)])
	


count = 0;
for i in range(1,1001):
	count += countDigit(str(i))
	
print(count)

	
