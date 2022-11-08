# Generator-functions return a genertor-object.
# If you call it explicitly and print it, you'll get __str__, as any other object.
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

print('Using list comprehension:')
t = [x for x in powers_of_2(4)]
print(t)

print('\nUsing list():')
l = list(powers_of_2(4))
print(l)

print('\nOperator in:')
for i in range(20):
    if i in powers_of_2(4):
        print(i)
