import py_compile
from module import sum1, prod1

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))

# Add a new path:
from sys import path
path.append('/home/gustavs/repo/Cisco-Python-Exercises/Python-2')
# Check Path:
for name in path:
    print(name)
# Test new path:
from module_test import resta
print(resta(4,5))