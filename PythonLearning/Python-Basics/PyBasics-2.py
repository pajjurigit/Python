# -*- coding: utf-8 -*-



g = input('Enter your name:')
g1 = input('Enter your age:')

print('Name:%s, Age as string:%s' %( g, g1))

print('Name:%s, Age in Int:%d' %( g, int(g1)))


num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))

print('Sum: ' + str(num1+num2))


#comparison
#relational operators return bool
print(100==100)
print('hello' = 'Hello') #false
print('a' > 'b')

#logical operators
hours = 39
salary = 39000

print((hours > 40) and (salary<=50000))

user='sdf'
pass1='Guest'

us=input('EnterPass:')
print(us==str.lower(pass1) or us==str.capitalize(pass1) or us==str.upper(pass1))

#if else
print('Enter the hours worked:')
hours = int(input())
rate = 25.0

if(hours > 40):
    grossPay = (40*rate) + (hours-40)* (rate*1.5) 
elif(hours > 40 and hours<50):
    grossPay = (40*rate) + (hours-40)* (rate*1.25) 
else:
    grossPay=(hours*rate)   
    
print('TotalPay:%.2f' % (grossPay))