# -*- coding: utf-8 -*-

#newton method of finding squre root

import math

def square(num):
    return num * num

def sqrt(num):
    return sqrtHelper(1.0, num)

def sqrtHelper(guess, num):
    if closeEnough(guess, num):
        return guess
    else:
        return sqrtHelper(improve(guess, num), num)
    
def closeEnough(guess, num):
    return (math.fabs((square(guess)) - num) < 0.001)

def improve(guess, x):
    return average(guess, x/guess)

def average(x,y):
    return (x+y)/2

print(sqrt(144))

    
#solving above sqrt logic using nested functions

def sqrtNested(number):
    def closeEnough(guess):
        return (math.fabs((square(guess)) - number) < 0.01)
    def improve(guess):
        return average(guess, number/guess)
    def sqrtHelper(guess):
        if closeEnough(guess):
            return guess
        else:
            return sqrtHelper(improve(guess))
    return sqrtHelper(1.0)

print (sqrtNested(144))

