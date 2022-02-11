# For example, if the client receives the Employee information in a long string, and details separated by the – (or any other delimiter). Instead of performing splitting operations from his end, we can create a Python class method and allow them to use it.

# In this example, we initialized fullname, age, gender, and salary. Next, we created a Python classmethod that split the given string based on – and returns those values. I suggest you refer to the split string article to understand the split function

class Employee:
    def __init__(self,name,age,gender,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary

    @classmethod
    def func_string_split(cls,employee_str):
        name,age,gender,salary=employee_str.split('-')
        return cls(name,age,gender,salary)

emp_from_cvs1='Suresh-27-male-130000'
emp_from_cvs2='John-27-male-150000'
emp_from_cvs3='Tracy-27-female-1365000'

emp1=Employee.func_string_split(emp_from_cvs1)
print(emp1.name)
print(emp1.age)
print(emp1.gender)
print(emp1.salary)

print()
emp3=Employee.func_string_split(emp_from_cvs3)
print(emp3.name)
print(emp3.age)
print(emp3.gender)
print(emp3.salary)