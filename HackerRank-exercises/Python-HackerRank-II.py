# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:02:23 2021

@author: pajjuri

LEARNINGS:
    -  Concentrate on reading a list from the input
    -  Observe the methods for finding Second Highest and Second Lowest numbers from a list
    -  Observe how to use Set and List vs Set differences
"""



# Find Next Lowest...
def findSecondHighest(numbers):
    #n=list(n)
    largest = float('-inf')
    large = float('-inf')
    for i in numbers:
        if i > largest:
            large = largest
            largest = i
        elif i > large and i != largest:
            large = i
    return large

print (findSecondHighest([10, 20, 30, 10, 9]))
print (findSecondLowest([51, 51, -50, 51]))

# Find Next Highest...
def findSecondLowest(numbers):
    smallest = float('+inf')
    small = float('+inf')
    for i in numbers:
        if i < smallest:
            small = smallest
            smallest = i
        elif i < small and i != smallest:
            small = i
    return small

print (findSecondLowest([10, 20, 30, 10, 9]))
print (findSecondLowest([-50, -50, 51, -50]))


##### 
#Print names of second highest score in alphabetical order...
#####

### Solution: 1
marksheet = []
for _ in range(int(input())):
    marksheet.append([input(), float(input())])
    #marksheet= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 35], ['Harsh', 39]]
    #sorted(list(set([marks for name, marks in marksheet])))
second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]

    for name, marks in sorted(marksheet):
        if marks == second_lowest:
            print (name)


### Solution 2:

marksheet = []

def findSecondLowest(numbers):
    smallest = float('+inf')
    small = float('+inf')
    for i in numbers:
        if i < smallest:
            small = smallest
            smallest = i
        elif i < small and i != smallest:
            small = i
    return small

for _ in range(int(input())):
    marksheet.append([input(), float(input())])

second_lowest = findSecondLowest([marks for name, marks in marksheet])

for name, marks in marksheet:
    if marks == second_lowest:
        print (name)


"""
### inputs
4
Rachel
-50
Mawer
-50
Sheen
-50
Shaheen
51

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""


## Take N number of students and their Marks (3 subjects) and display the average (two decimal) of the
## student queried...
### LEARNINGS:
    ### Concentrate on reading inputs of marks (name and list of marks) and creating a dictionary out of it
    ### Concentrate on Print formatting for displaying always 2 digits

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query = input()

markList = list(student_marks[query])
#print(round(sum(markList)/len(markList),2))

#If output must show you 2 digits in all the cases...
print("{0:.2f}".format(sum(markList)/len(markList)))
#Or
print('%.2f' %(sum(markList)/len(markList)))


### Use regex to validare a credit card
'''
Valid Credit card rules
► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
'''

import re #must be imported for regular rexpressions

ccList = []
n = int(input())
for _ in range(n):
    ccList.append(str(input()))

def isValidCC(nbr):
    ret = False
    #regProg = re.compile("^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$")
    regProg = re.compile(
            r"^"
            r"(?!.*(\d)(-?\1){3})"
            r"[456]"
            r"\d{3}"
            r"(?:-?\d{4}){3}"
            r"$")
    if regProg.search(nbr):
        ret = True
    if ret:
        return 'Valid' 
    else:
        return 'Invalid'

resList = list(map(isValidCC, ccList))

print("\n".join (resList))