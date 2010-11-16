 s = [str(i) for i in range(1,1000001)]
>>> s = "".join(s)
>>> s[1]
'2'
>>> s[0]
'1'
>>> int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])