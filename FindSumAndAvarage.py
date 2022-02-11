#  Instead of printing the message, we are finding the sum and average. First, we created a Static Method that accepts three arguments and returns some of those three. Next, we defined a Python classmethod that calls the static method using the cls. Within the function, it finds returns the average of static method result.

class Employee:

    company='avator'

    @staticmethod
    def add(a,b,c):
        return a+b+c

    @classmethod
    def avg(cls):
        x=cls.add(10,20,30)
        return(x/3)

average=Employee.avg()
print('The Average of three Numbers=', average)