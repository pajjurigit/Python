# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:01:48 2021

@author: pajjuri
"""
# Pyhon Challenges - Hacker Rank Learning
cube = [[i for i in range(3)] for _ in range(6)]

 #inputs
x =1
y=1
z=2

n =3

#print cube where 0<=i<=x; 0<=j<=y; 0<=k<=z and sum of i+j+k should not be equal to n
# This will create the list all possible combinations of cube of 1,1,2 
hackerCube = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) ]
print(hackerCube)

#This will filter all the combos addition of three elements equal to n
hackerCube = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n) ]
print(hackerCube)



