# Exceptions are classes:
try:
    integer = int('I am an integer for sure')
except Exception as e:
    print(e) # => invalid literal for int() with base 10: 'I am an integer for sure'
    print(e.__str__()) # Same as above.

# All exceptions are part of a hierarchy of classes:
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1) # Recursion

print_exception_tree(BaseException)