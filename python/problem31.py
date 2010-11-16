def p(x):
	return 1

def p2(x):
	if x >= 0: return p2(x-2) + p(x) 
	return 0

def n(x):
	if x >= 0: return n(x-5) + p2(x)
	return 0

def d(x):
	if x >= 0: return d(x-10) + n(x)
	return 0

def q(x):
	if x >= 0: return q(x-20) + d(x)
	return 0

def c(x):
	if x >= 0: return c(x-50) + q(x)
	return 0

def b(x):
	if x >= 0: return b(x-100) + c(x)
	return 0

print(b(200))