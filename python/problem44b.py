#much better cleaner solution...Don't need to use combinations...

import sys
 
pentagonals = {}
for n in range(1,10000) :
    pent = n*(3*n-1)/2
    pentagonals[pent] = True
 
    for pent2 in pentagonals.keys() :
        if (pent - pent2) in pentagonals:
            pent3 = pent - pent2
            if (abs(pent2 - pent3)) in pentagonals:
                print (pent2, pent3, abs(pent2 - pent3))
                sys.exit()

