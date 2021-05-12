# -*- coding: utf-8 -*-

#assigning functions to variables

def square(num):
    return num*2

num=2
sqnum = square(num) #simply executes the value and stores the result in sqnum

sqnbr = square #this is assignment of a function to a variable

sqnbr(num) #this will return the value of the square of the number

print(sqnbr(num))



#higher order functions
#usually involves function calling another function to map...
#ex: map, filter and reduce are some examples of higher order functions
#map function

nbrs = [1,2,3,4]

#map, maps the list of nbrs to the square function and creates the list out of it using list function
nbrsqrsList = list(map(square, nbrs)) 
print(nbrsqrsList)


#anonymous functions
sqrLam = lambda x: x*x
sqrLam (10)


numbersq = [2,3,5,6,8]
numsqrslistq = list(map(lambda x: x*x, numbersq))
print(numsqrslistq)