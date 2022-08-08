# import math => math.sin / math.pi

from math import * # Yes, it does work. Just pay more attention. No need of "math."
# There is not any conflicts since there are two namespaces. 
# One in which I created sin() and pi and other which was imported.

# Using alias
# import math as m

# print(m.sin(m.pi/2))

def sin(x):
    if 2 * x == pi:
        return 1
    else:
        return None

pi = 3.14

print(sin(pi/2)) 
print(sin(pi/2))