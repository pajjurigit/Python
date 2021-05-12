# -*- coding: utf-8 -*-

# importing user defined modules
# * denotes importing all functions...


'''from newton import *

print('Enter a number: ')
num = int(input())

print(sqrt(num))

print(sqrtNested(num))

print(average(5,6))'''


#importing speciifc functions instead of whole module
#you use this way, so that you dont have to qualify the methods with namespace name
from newton import average, square

print(average(53,65))
print(square(81))

import newton
print(newton.sqrt(144))


