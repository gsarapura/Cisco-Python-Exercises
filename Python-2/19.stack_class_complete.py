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
        Stack.__init__(self) # In Python, you must explicitly invoke superclass constructor.
        self.__sum = 0
    # Push method must add variable to sum and use push method from superclass.
    # Besides, the only way to access stack_list is through superclass.
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    # Pop method must remove variable from sum and use pop method from superclass.
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    def get_sum(self):
        return self.__sum

stack_object = AddingStack()

stack_object.push(2)
stack_object.push(89)
stack_object.push(233)
stack_object.push(10)
stack_object.push(41)

stack_object.pop()
stack_object.pop()
print("Total sum:", stack_object.get_sum())