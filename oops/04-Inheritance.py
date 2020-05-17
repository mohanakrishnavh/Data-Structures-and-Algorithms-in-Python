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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if len(self.employees) == 0:
            print("No Employees.")
        else:
            for emp in self.employees:
                print("-->", emp.fullname())


# Before defining the Developer class
dev_1 = Developer("Pranam", "Thomas", 50000, "NULL")
dev_2 = Developer("Arshi", "Shiyal", 60000, "NULL")
# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print()

dev_3 = Developer("Shyam", "Sundar", 50000, "Python")
dev_4 = Developer("Arun", "Kumar", 60000, "Java")
print(dev_3.email)
print(dev_3.prog_lang)
print(dev_4.email)
print(dev_4.prog_lang)
print()

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
print()
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emps()
print()
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

print()
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print()
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
