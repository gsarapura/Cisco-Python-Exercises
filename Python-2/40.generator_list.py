print('\nAny comprehension can be turned into a generator and viceversa:')
print('Curly braces for comprehensions and parenthesis for generators:')
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

print('\nYou can check the len to see whether it is a list or not:')
try:
    print('Length of list:', len(the_list))
    print(len(the_generator))
except Exception as e:
    print('TypeError:', e)

print('\nDirectly:')
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()
