class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)

    def apply_raise(self):
        # we cal also use Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Pranam", "Thomas", 50000)
emp_2 = Employee("Arshi", "Shiyal", 60000)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Namespace
print(emp_1.__dict__)
print(Employee.__dict__)

# Changes reflect to the class and all instances
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.__dict__)

# Employee count
print(Employee.num_of_emps)
