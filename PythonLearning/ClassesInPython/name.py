# -*- coding: utf-8 -*-

class Name:
    #constructor methods - instantiation
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
        
    #to-string method
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last
    
    def lastToFirst(self):
        return self.last + ',' + self.first + ' ' + self.middle
        
    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]
        
    

aName = Name('John', 'B', 'Doe')
print(aName.first, aName.middle, aName.last)

#this will print properly, because the internal str method is overridden in the Name Class
print(aName)
print('aName is: ' + str(aName))
print ('aName Last,First M: ' + aName.lastToFirst())
print('aName initials: ' + aName.initials())