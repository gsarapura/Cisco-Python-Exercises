import math

# from math import * This ain't working.

# There is not any conflicts since there are two namespaces. 
# One in which I created sin() and pi and other which was imported.

def sin(x):
    if 2 * x == pi:
        return 1
    else:
        return None

pi = 3.14

print(sin(pi/2)) 
print(math.sin(math.pi/2))