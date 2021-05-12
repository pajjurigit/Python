# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:01:48 2021

@author: pajju
"""
# Pyhon Challenges - Hacker Rank Learning

cube = [[i for i in range(3)] for _ in range(6)]

x =1
y=1
z=2

n =3

#print cube where 0<=i<=x; 0<=j<=y; 0<=k<=z and sum of i+j+k should not be equal to n
hackerCube = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n) ]

print(hackerCube)



#Print names of second highest score in alphabetical order...



rec=[]
recsOut=[]
names=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    rec=[name, score]
    recsOut.append(rec)
    
def findSecondLowest(n):
    mx = n[0]
    nMx = n[1]
    
    for i in range(2, len(n)):
        if n[i] > mx:
            nMx = mx
            mx = n[i]
        elif n[i] > nMx and mx != n[i]:
            nMx = n[i]
    return nMx

recsOut= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 35], ['Harsh', 39]]

#scs=[score[1] for score in recsOut]
#OR
scs = [score for name, score in recsOut]

#findSecondLowest([score[1] for score in recsOut])
secHighest = findSecondLowest(scs)

print(scs)
print(secHighest)

names=[]
for i in recsOut:
        if i[1] == secHighest:
            names.append(i[0])
            
names.sort()
for i in names:
    print(i)

