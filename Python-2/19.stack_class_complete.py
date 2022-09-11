# Define class:
class Stack:
    # Define constructor:
    def __init__(self):
        self.__stack_list = []
    # Push method:
    def push(self, val):
        self.__stack_list.append(val)
    # Pop method:
    def pop(self):
        val = self.__stack_list[-1]
        self.__stack_list.pop(-1)
        return val

# Define subclass that will sum all elements of stack:
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())



