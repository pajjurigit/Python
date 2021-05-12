# -*- coding: utf-8 -*-

grades = [71, 80, 94, 78]

print (grades)
for i in range(len(grades)):
    grades[i] = grades[i]+5
print (grades)
    
#looping through list elements in the list statments
grades = [grade+5 for grade in grades]
print(grades)

words = ['NOW' ,'HI','CAP','LINE']

words = [word.lower() for word in words]
print (words)


#files
#regular way of reading a file

file = open('outGrades.dat')
grades = file.readlines()
print(grades)

grades = [grade.rstrip() for grade in grades]
print(grades)

grades = [int(grade)+5 for grade in grades]
print (grades)

grades = [grade.rstrip() for grade in open('outGrades.dat')] #file open is nothing but a sequence of data...
print(grades)


#Exercise

#find even numbers in a range

N=range(1,101) #range returns list and store it in a list var
Niter = iter(N) #to iterate manually through the list...

allEvens = [x for x in N if x%2==0]
allOdds = [x for x in N if x%2!=0]

print('allEvens: ', allEvens)
print ('allOdds: ', allOdds)


#print all the words lengths in a sentence
sentence = 'Now is the time to see who got whats worth'
sentList = sentence.split(' ')

allLengths = [len(w) for w in sentList]
print(allLengths)


allwTuples = [(word, len(word)) for word in sentList]
print(allwTuples)

allDicts = [{word: len(word)} for word in sentList]
print(allDicts)

allLists = [[word, len(word)] for word in sentList]
print(allLists)


