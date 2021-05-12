# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        
    def __str__(self):
        return 'name: ' + self.name + ' sex: '+ ' age: ' +self.sex + ' ' + str(self.age)
    
    def changeName(self, name):
        self.name = name
        
    def incrementAgeby1(self):
        self.age = self.age+1
    
    
person1 = Person('Jane Doe', 'F', 23)
person2 = Person('Bob Smith', 'M', 35)

print('Person 1 details:\n ' + str(person1))

person1.incrementAgeby1()
print('After changing the age')
print('Person 1 details:\n ' + str(person1))