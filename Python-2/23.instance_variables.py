# Instance variables: if the value of the variable varies form object to object.
# Class variables: It is declared inside of a class, but outside of any instance method or __init__ method.

class Student():
    # It is always the same value in all objects.
    adding_counter = 0
    # Constructor:
    def __init__(self, name = 'Jorge', age = 19):
        # Instance variables:
        self.__name = name # Whether it is private or pubclic, the display changes accordingly.
        self.__age = age 
        self.__subjects = []
    def add_subject(self, subject):
        self.__subjects.append(subject)
        Student.adding_counter += 1
        
s1 = Student()
s2 = Student('Emiliano', 20)
s3 = Student(age = 21)

s2.add_subject('Sistemas operativos')

s3.__address = 'Arquímides 435'

# Class variables are not shown in __dict__ since they are not part of an object.
print(s1.__dict__, s2.adding_counter) 
print(s2.__dict__, s2.adding_counter)
print(s3.__dict__, s3.adding_counter)
# For class variables:
print(Student.__dict__)