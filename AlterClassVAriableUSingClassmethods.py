# Alter class variable using clasmethod in Python
# In this example, we are going to create a Python classmethod that accepts an argument and assigns the value to the class variable. It means, when you call this function, it replaces the company text with the new text that you provide as an argument value. It helps to hide the class variables and allows the end-users to work with the variable.


class Employee:
    company='Avator'

    @classmethod
    def func_newName(cls,new_Name):
        cls.company=new_Name

emp=Employee()

print(Employee.company)
print(emp.company)

print()
Employee.func_newName('Coding')

print(Employee.company)
print(emp.company)
