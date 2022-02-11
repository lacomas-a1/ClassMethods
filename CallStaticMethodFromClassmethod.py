# Call Static Method from classmethod in Python
# In this staticmethod example, we show how to call Static Methods within the class method. Here, we created a staticmethod called func_msg(), which prints a welcome message. Next, we defined the message that returns a class variable company and the name. Within the same function, we are calling the staticmethod using the cls.methodname.

class Employee:
    company='Avator'

    @classmethod
    def message(cls):
        print('The company Name is %s' %cls.company)
        print('The message is from %s Class' %cls.__name__)
        cls.func_msg()

    @staticmethod
    def func_msg():
        print('Wwelcome to python Programming')

Employee.message()