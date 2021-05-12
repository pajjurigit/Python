
class Employee:
    
    def __init__(self, name, payRate):
        self.name = name
        self.pay = payRate
        
    def __str__(self):
        return 'EmpName: ' + self.name + 'EmpPay: ' + str(self.pay)
    
    def grossPay(self, hoursWorked):
        return self.pay * hoursWorked
    

class Manager(Employee):
    def __init__(self, name, payRate, isSalaried):
        Employee.__init__(self, name, payRate)
        self.isSalaried = isSalaried
        
    def __str__(self):
        retStr = Employee.__str__(self)
        retStr += ' Salaried: ' + str(self.isSalaried)
        return retStr
    
    def grossPay(self, hours):
        if self.isSalaried:
            return self.pay
        else:
            return self.pay * hours
        

    
    
e1 = Employee('John Doe', 20)
print (e1)
print('Gross Pay: ' + str(e1.grossPay(40)))

m1 = Manager('Jane Sus', 2500, True)
print(m1)
print('Gross Pay: ' + str(m1.grossPay(45)))

m2 = Manager('Sam Adams', 35, False)
print(m2)
print('Gross Pay: ' + str(m2.grossPay(45)))

#Displaying all employees that are stored in a list

empList = [e1, m1, m2]
for emp in empList:
    print(emp)
    
    