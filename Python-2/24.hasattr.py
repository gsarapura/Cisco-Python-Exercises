# Not all the objects will have the same attributes. You can check it wiht hasattr() function.
class Real_numbers():
    a = 1
    def __init__(self, value):
        if value % 2 != 0:
            self.odd = 'yes, it is odd!'
        else:
            self.even = 'yes, it is even!'
n = Real_numbers(2)
print(n.even)

# If it does not have that attribute => AttributeError
# This is a solution but it is not sufficient.
# try:
#    print(n.odd)
# except AttributeError:
#    pass
# hassattr() waits for two arguments:
if hasattr(n, 'odd'):
    print(n.odd)
# hassattr() works with class variables also (it return a boolean value):
print(hasattr(Real_numbers, 'a'))
print(hasattr(Real_numbers, 'b'))

