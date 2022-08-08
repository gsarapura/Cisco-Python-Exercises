from random import random, seed 
# random = 0 to 1
# seed => int_value
seed(0)

for i in range(4):
    print(random())

from random import randrange, randint

print(randrange(-1), end=' ') # Negative numbers are not allowed
print(randrange(0, 10), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 29))

# The problem with the previous functions is that numbers can be repeated.
# To avoidad that:

from random import choice, sample 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(choice(my_list))
print(sample(my_list, 9))
print(sample(my_list, 5))