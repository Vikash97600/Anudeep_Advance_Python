class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.Salary = salary  # Uses the setter to validate and set _salary
    
    # getter method
    @property
    def salary(self):
        return self.Salary
    
    # setter method
    @salary.setter
    def salary(self, newSalary):
        if newSalary >= 0:
            self.Salary = newSalary
        else:
            raise ValueError("Salary cannot be negative.")
    # delter method
    @salary.deleter
    def salary(self):
        print(f"Delete salary for {self.name}")
        del self.Salary

emp = Employee("Vikash", 5000)
print(emp.salary)  # Output: 5000
emp.salary = 6000
print(emp.salary)  # Output: 6000
del emp.salary
# Trying to access emp.salary after deletion will raise AttributeError
# print(emp.salary)