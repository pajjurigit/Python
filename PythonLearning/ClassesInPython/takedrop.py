# -*- coding: utf-8 -*-

import math

def take(num, lst):
    rlist=[]
    if num > 0:
        for i in range(0, num):
            rlist.append(lst[i])
    else:
        #you can also use reversed(<list>) function here...
        lst.reverse()
        for i in range(0, (-1*num)):
            rlist.append((lst[i]))
        lst.reverse()
        
    return rlist

def drop(num, lst):
    rlist=[]
    if num > 0:
        for i in range(num, len(lst)):
            rlist.append(lst[i])
    else:
        lst.reverse()
        for i in range((-1*num), len(lst)):
            rlist.append(lst[i])
        lst.reverse()
        
    return rlist

#geting Even indexed elements from the list
def getEvenIndexElementsFromList(lst):
    res=[]
    for idx, ele in enumerate(lst):
        print(str(idx) + ' '  + str(ele))
        if idx % 2 == 0:
            res.append(lst[idx])
    return res
print(getEvenIndexElementsFromList(names))

names=['james', 'amy','adam','nestor','vlad','tricia','tracy','wendy']

#easy methods to read from Nth elements from the list
print(names[5:]) #lists out elements from 5th index to end

#easy methods to read last N elements from the list
print(names[-5:]) # lists out last 5 elements of the list, if index is out of range, lists all elements

print(take(3, names))

print(drop(4, names))
        
print(take(-3, names))
print(names)

print(drop(-4, names))

print(names)

def takeFromEnd(lst):
    for i in range(-1, num):
        print(lst[i])



