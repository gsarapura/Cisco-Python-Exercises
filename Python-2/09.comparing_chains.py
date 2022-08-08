# Operators:
print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabet')
print('beta' > 'Beta')

# Chains made of digits:
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

# Comparing numbers and strings is not a good idea.
# But == and != are allowed, the rest will give TypeError:
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
print('10' > 10)

# Order:
# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
# Different lists.
print(first_greek)
print(first_greek_2)

# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
# Same list.
second_greek.sort()
print(second_greek)