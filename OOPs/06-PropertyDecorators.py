class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{0}.{1}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        # we cal also use Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Shyam", "Sundar", 50000)
emp2 = Employee("Arun", "Kumar", 60000)

emp1.first = 'Jim'
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

emp1.fullname = 'Corey Schafar'
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)
