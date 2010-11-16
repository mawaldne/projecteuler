nums = [a**b for a in range(0, 101) for b in range(0, 101)]

l = [];
for num in nums:
	l.append(sum([int(a) for a in str(num)]))

print(max(l))

'''or'''
max( [ sum( [ int( i ) for i in str( a ** b ) ] ) for a in xrange( 90, 100 ) for b in xrange( 90, 100 ) ] )
	

		