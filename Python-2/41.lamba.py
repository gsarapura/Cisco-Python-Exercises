from rich.console import Console
console = Console()

console.print("[i]Regular declaration[/i]")
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

console.print("\n[i]Lambda declaration[/i]")
def print_function2(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function2([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

"""
map(function, iter):
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
It returns a map object that can be, for example, passed to list() to create a list, duh. 
"""
console.print("\n[i]Map + lambda declaration[/i]")
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

"""
filter(function, sequence)
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
It return an iterator that has already been filtered
"""
console.print("\n[i]Filter + lambda declaration[/i]")
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)


