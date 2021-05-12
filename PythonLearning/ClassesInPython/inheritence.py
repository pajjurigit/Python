# -*- coding: utf-8 -*-

#Inheritence
#is-a relationship
#manager is-a employee
#car is-a vehicle
#rectangle is-a shape

class Shape:
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
        
    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y) + '\n'
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
class Rectangle(Shape):
    
    def __init__(self, xcor, ycor, wth, ht):
        Shape.__init__(self, xcor, ycor)
        self.w = wth
        self.h = ht
        
    def __str__(self):
        retStr = Shape.__str__(self)
        retStr += 'width: ' + str(self.w) + ' height: ' + str(self.h)
        return retStr
        
rec = Rectangle(5,10,8,9)

print (str(rec))
rec.move(10, 12)
print(rec)

