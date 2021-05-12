# -*- coding: utf-8 -*-

#while

#count controlled while loop
num = 1
while num<=10:
    print(num)
    num=num+1
    
num = 1
sum1=0
while num<=10:
    sum1 = sum1+num
    num=num+1

print('sum:%d' %sum1)


balance = 10000
rate = 3.7
year=1
while year <= 30:
    balance = balance *rate
    print('year:%s balance:%.2f' %(year, balance))
    year=year+1
    
     
#event controlled while loop
avg=0.0
total=0
count=0

print('Enter the Grade (-1 to quit): ')
grade = int(input())

while grade!=-1:
    total=total+grade
    count=count+1
    print('Enter the Grade (-1 to quit): ')
    grade = int(input())
    
avg = total/count
print('Avg of all grades entered:%.2f' % avg)

#continue
num = 0;
denom=0;
while num != -1 or denom != -1:
    print('enter enumerator  (-1 to exit)::')
    num = float(input())
    if(num == -1):
        break
    print('enter denom (-1 to exit):')
    denom=float(input())
    if denom==-1:
        break
    
    if denom == 0:
        continue
    print(num/denom)
    
