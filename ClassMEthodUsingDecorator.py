class Employee:
    company='Avator'

    @classmethod
    def message(cls):
        print('The message is from %s Class' %cls. __name__)
        print('The company Name is %s' %cls.company)

Employee.message()

print()
Employee().message() 

# we are creating a class method called message using the Python @classmethod decorator. Within this method, cls.__name__ returns the class name (Employee), and cls.company returns the class variable company value (Tutorial Gateway).#Other way of calling