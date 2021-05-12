# -*- coding: utf-8 -*-

import functools

def squares(num):
    return num * num

def even(num):
    if num %2 == 0:
        return True;
    else:
        return False;
    
def sums(x,y):
    return x+y

numsList = [1,2,3,4,5,6]

#map
numsSqrsList = list(map(squares, numsList))
print(numsList)
print(numsSqrsList)

#filter
numsRange = list(range (1,50))
evens = list(filter(even, numsRange))
print(evens)

#reduce
numsForReduce = list(range(1,15))
print(numsForReduce)
sums = functools.reduce(sums, numsForReduce)
print('sum of the range above is %d' %sums)


#count the letters in a list of words
def countListLetters(words):
    if len(words) < 1:
        return 0
    else:
        return len(words[0]) + countListLetters(words[1:])

sentence = ['now', 'is', 'the', 'time', 'for', 'all']
print(str(countListLetters(sentence)))

#words into acronyms

def first(word):
    #return str.capitalize(word[0])
    return word[0]

words = ['in', 'my', 'humble', 'opinion']

#acro=''
#acro = acro.join(list(map(first, words)))
def acronym(words):
    acro=''
    acro = acro.join(list(map(first, words))).upper()
    return acro

#acro = ''
#acro = acro.join(list(map(first, words))).upper()
acro1 = acronym(words)
print(acro1)








