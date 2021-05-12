# -*- coding: utf-8 -*-

import os;

square = ((10,8), (10,23), (25,23), (25,8))

print('print points with For' )
for pts in square:
    print(pts)
    
#print it with iter

print('print points with Iter....')
ptsIter = iter(square)

print(next(ptsIter))
print(next(ptsIter))
print(next(ptsIter))
print(next(ptsIter))


