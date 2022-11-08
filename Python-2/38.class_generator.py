"""
Fibonacci series:
    Fib1 = 1
    Fib2 = 1
    Fib3 = Fib1 + Fib2
    ...
    Fib(n) = Fib(n-2) + Fib(n-1) 
"""
class Fib:
    def __init__(self, nn):
        print("__init__") # For tracking methods. 
        self.__n = nn # Limit of a series.
        self.__i = 0 # Tracking actual number of a series.
        self.__p1 = self.__p2 = 1 # To keep the last two numbers
    
    # Iterator object is initialise:  
    def __iter__(self):
        print("__iter__")
        return self
    
    # Starts iteration
    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
"""
You cannot explicitly call it since it is an object.
If you do it, you'll get the object __str__.
"""

# Using a class
class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(2)

for i in object:
    print(i)

print('\nBetter version')
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
