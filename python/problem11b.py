# This was a pretty cool solution...I should look into numpy...

from numpy import *
grid = [[ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
# ...
        [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]]
grid = array(grid)
 
horiz = max(prod(grid[i,j:j+4]) for i in range(20) for j in range(17))
vert = max(prod(grid[i:i+4,j]) for i in range(17) for j in range(20))
d1 = max(prod(diag(grid[i:i+4,j:j+4])) for i in range(17) for j in range(17))
d2 = max(prod(diag(grid[i:i+4,j+4:j:-1])) for i in range(17) for j in range(17))
print max(horiz, vert, d1, d2)


# Heres another good one:

def max_product(gridStr, num=4):
    # convert gridStr to a 2 dimensional matrix
    # each element can be accessed: grid[row][col]
    # 'num' is the number of numbers to multiply
    grid = [[int(i) for i in row.split()] for row in gridStr.split('\n')]
 
    # calculate products on each row
    rowList = [reduce(mul, row[j:j+num]) for row in grid for j in range(len(row)-num+1)]
 
    # calculate products on each col
    colList = [reduce(mul, [grid[j+k][i] for k in range(num)]) \
                for j in range(len(grid)-(num-1)) for i in range(len(grid[0]))]
 
    # calculate products on diagonal left high to right low
    diagList1 = [reduce(mul, [grid[j+k][i+k] for k in range(num)]) \
                 for j in range(len(grid)-(num-1)) for i in range(len(grid[0])-(num-1))]
 
    # calculate products on diagonal left low to right high
    diagList2 = [reduce(mul, [grid[j-k][i+k] for k in range(num)]) \
                 for j in range(len(grid)-1, num-2, -1) for i in range(len(grid[0])-(num-1))]
 