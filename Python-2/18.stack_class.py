""" Stack class:
1. Must have a property similar to the previous stack: any object must have a new list
which can not be shared betweeen objects.
2. The list must be hidden from the class's users.
    In order to achieve these: constructor.
"""
class Stack: # Defines the class.
    def __init__(self): # Defines the constructor method.
        self.__stack_list = [] # We canhide stack_list with __ (encapsulation)

stack_object = Stack() # Instantiates an object.
print(len(stack_object.stack_list)) 



