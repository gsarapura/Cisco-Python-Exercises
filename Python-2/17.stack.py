# Stack is a data structure that stores items in Last-In/First-Out manner.

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    stack.pop(-1)
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

# The problem with this is that anyone can destroy the stack by changing the values with stack[0] = 0, for example.
# POO brings a solution: encapsulation.