# -*- coding: utf-8 -*-

def numVowels(string):
    string = string.lower()
    count = 0;
    for i in range(len(string)):
        if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
            count = count+1
    return count

vowCnt = numVowels('Hi there, how Are You? I am doing fine by he way!!!')

print('num of Vowels: %d' %vowCnt)



#predicate functions -- always return true or false values

def isVowel(letter):
    if letter=='a' or letter=='e' or \
        letter=='i' or letter=='o' or letter=='u':
            return True
    else:
        return False

def numValwithPredFunc(string):
    string = string.lower()
    count=0;
    for i in range(len(string)):
        if isVowel(string[i]):
            count += 1
    return count

print('vowel count:%d' % numValwithPredFunc('Hello India!!, How are things there, we are fine here in US!'))


#function Exercises
#0-240 -- 0%; 24-481 -- 15%; 481 or greater - 28%

def tax(amount):
    if amount < 240:
        return amount
    elif amount >= 240 and amount < 481:
        return amount * 0.15
    elif amount >= 481:
        return amount * 0.28


def netPay(grossAmount):
    return grossAmount - tax(grossAmount)

print ('Enter Amount: ')
amnt = float(input())

print('Tax for the amount is: %.2f' % tax(amnt))
print('NetPay for the amount is: %.2f' %netPay(amnt))


#Recursion
def fact(nbr):
    if nbr <=1:
        return 1
    return nbr * fact(nbr-1)

print('Enter Number:')
num = int(input())

print('factorial of a %d is: %d' %(num, fact(num)))

def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])
print ('Enter the word:')
word = input()
print(explode(word))

def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])
    
print ('Enter the word:')
word = input()
print(removeDups(word))
        












