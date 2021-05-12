# -*- coding: utf-8 -*-


#for

nums = [1,2,4,5,6]
sum = 0
for x in nums:
    sum = sum+x  
print(sum)

word = 'hello'
for letter in word:
    print(letter)
    
sentence = 'Now is the time for all good people to come to the aid'
count=0
for letter in sentence:
    if letter == 'a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count=count+1
        
print('Vowels in the sentence: %d' %count)

sum=0
numtups = (6,7,4,8,9,4)
for tup in numtups:
    sum=sum+tup
    
print('sum of the tuples:%d' %sum)
    
words = ('now','is','the','time', 'change', 'it')

max=0
for i in range (1,len(words)):
    if len(words[i]) > len(words[max]):
        max=i
print('the max word is:%s' % words[max])


for line in open('outGrades.dat'):
    print(line, end='') #end removes extra line feed by the for loop...
    
    