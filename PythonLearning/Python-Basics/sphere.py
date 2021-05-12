# -*- coding: utf-8 -*-

pi = 3.14159


def square(num):
    return num*num

def cube(num):
    return square(num)*num

def area(radius):
    return 4 * pi * square(radius)

def volume(radius):
    return (4.0/3.0) * pi * cube(radius)



