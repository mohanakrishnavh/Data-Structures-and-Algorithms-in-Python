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

    def __repr__(self):
        '''
        Returns unambiguous representation of the object. Used for Debugging & logging.
        '''
        return "Employee('{0}','{1}',{2})".format(self.first, self.last, self.pay)

    def __str__(self):
        '''
        Returns a more readable form for the end user
        '''
        return "{0} - {1}".format(self.fullname(), self.email)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Shyam", "Sundar", 50000)
emp2 = Employee("Arun", "Kumar", 60000)
print(emp1) # will call __str__ which will call __repr__ if it is empty

print(repr(emp1))
print(str(emp1))

print(emp2.__repr__())
print(emp2.__str__())


print(1+2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp1+emp2)

print(len('test'))
print(str.__len__('test'))

print(emp1.fullname())
print(len(emp1))
