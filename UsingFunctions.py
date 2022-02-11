#  we are using the Python classmethod() function to create a class method. From the below Python code, the Employee.printValue statement convert the function to this.

# 

class Employee:
    value=100

    def printVAlue(cls):
        print('The Value=%d' %cls.value)

Employee.printVAlue=classmethod(Employee.printVAlue)
Employee.printVAlue()