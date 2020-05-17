import datetime


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

    # regular method
    def apply_raise(self):
        # we cal also use Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Pranam", "Thomas", 50000)
emp_2 = Employee("Arshi", "Shiyal", 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.06)
print(Employee.raise_amount)
print(Employee.__dict__)
print(emp_1.raise_amount)
print(emp_1.__dict__)
print(emp_2.raise_amount)
print(emp_2.__dict__)

print()
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)
print()

# class methods as alternate constructor
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_2.email)
print(new_emp_2.pay)
print()
print(new_emp_3.email)
print(new_emp_3.pay)
print()

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))


