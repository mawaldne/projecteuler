num = [1]
list = [3,5,7,9]
startSize = 3
endSize = 1001

while (startSize <= endSize):
	startSize += 2
	num.extend(list)
	list = [list[3] + (i * (startSize-1)) for i in range(1,5)]

print(sum(num))




