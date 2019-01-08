class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)


emp_1 = Employee("Pranam", "Thomas", 50000)
emp_2 = Employee("Arshi", "Shiyal", 60000)


# Employee Objects
#print(emp_1)
#print(emp_2)

print(Employee.fullname(emp_1))
print(emp_2.fullname())
