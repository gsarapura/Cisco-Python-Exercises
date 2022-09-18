# Instance variables: if the value of the variable varies form object to object.
# Class variables: It is declared inside of a class, but outside of any instance method or __init__ method.

class Student():
    # Constructor:
    def __init__(self, name = 'Jorge', age = 19):
        # Instance variables:
        self.__name = name # Whether it is private or pubclic, the display changes accordingly.
        self.__age = age 
        self.__subjects = []
    def add_subject(self, subject):
        self.__subjects.append(subject)
        
s1 = Student()
s2 = Student('Emiliano', 20)
s3 = Student(age = 21)

s2.add_subject('Sistemas operativos')

s3.__address = 'Arquímides 435'

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

