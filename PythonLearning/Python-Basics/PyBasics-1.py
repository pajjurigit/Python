# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:26:34 2020

@author: pajju
"""


import this
import math
import random
import sys

#print function

wrd = 'hello'
num=456
print(wrd, num)
print(wrd+' ' +str(num))

sys.stdout.write('hello\n')

#sending print to a file...

#--- Uncommenting below line would print all the statements into a output.dat file....
#sys.stdout = open('output.dat','a')


#Printing on same line in python 3.0
n=9
for i in range (1, n+1):
       print(i, end="")


n='Mary'
grade = 81.7865
#record = '%s: %.2f',

#format strings
print('%s: %.2f' % (n, grade))


print("Hi Py!!!")

print("pow--")
print(pow(2,3))

print("abs--")
print(abs(-1))

print("round--")
print(round(2.809034, 2))
print(round(2.809034))

#math lib--
print('math----')
print(math.sqrt(9))

print(math.floor(2.5))

print('math end----')

#rand lib
print('random and random int')
print (random.random())
print(random.randint(1,1000))

#strings--

print('strings---')
print(len('hi how are you?'))

str = 'Hi There!!';
print(len(str))
print(str[0])
print(str[1:5])
print(str[:7])
print(str*2)
print(str[4:])
str1='now, is, the, time,!'
print(str1.split(',')) # returns a list

print(str.strip())
print(str.rstrip())


#lists
nums=[2,3,5,6]
print (nums)
print(nums[0]+nums[2]+nums[3])
print(nums[0:2])
print(len(nums))


words = ['ho', 'ho']
words1 = ['ha', 'ha']
print(words+words1)

wordrep = ['hello']
print(wordrep*5)

nestList = ['hi', 'how', ['are', 'you'], 'thanks']
print(nestList[2])


#dictionaries

dict1= {'john':233, 'joy':243}
print(dict1)
print(dict1['john'])
print(dict1.keys())
print(dict1.values())

#Tuples
#immutable unlike list
#you can use tuples as keys in the dictionary

numts = (1,2,4,5,8)
#print(numts(0))
print(len(numts))
print (numts[1]+numts[2]+numts[3])
print(numts[1:4])

numts1 = (5,6)
print(numts+numts1)







