# -*- coding: utf-8 -*-

#fields - name, id, grades(list)

class Student:

    grades = []
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def addGrades(self, grade):
        self.grades.append(grade)
        
    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

    def __str__(self):
        return '  Name: ' + self.name + '\n' +\
                '  ID: ' + self.id + '\n' + \
                '  Grades: ' + self.showGrades()
    
    def avgGrade(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total/len(self.grades)
    
    
    
    
stu1 = Student('John', '123')
stu1.addGrades(88)
stu1.addGrades(98)
stu1.addGrades(78)

print(stu1.showGrades())
print('Student Details: \n' + str(stu1))
print('Avg of grades: %.2f' % stu1.avgGrade())