# -*- coding: utf-8 -*-

try:
    print('enter a number')
    num = int (input())
    print('enter a denom')
    denom = int (input())
    print(str(num/denom))
    
    #you can raise the exceptions as follows
    #raise ZeroDivisionError
    
except ZeroDivisionError:
#except IOError:

    print('Cannot divide by zero')
    
    print('enter a number')
    num = int (input())
    print('enter a denom')
    denom = int (input())
    print(str(num/denom))
    

try:
        print('enter a file name')
        name = input()
        file = open(name, 'w')
        display(file)
except IOError:
    print('Error with file')
    print('enter a file name')
    name = input()
    file = open(name, 'w')
    display(file)

finally:
    file.close()
    


