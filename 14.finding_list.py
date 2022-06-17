#Finding a number in the list.

lista_one = [2, 3, 4, 5, 6]
to_find = int(input("Type in the number you are looking for: "))
found = False

for i in lista_one:
    if i == to_find:
        found = True
        break #This is what I find really interesting.

if found:
    print(f'We have found {to_find} in the list.')
else:
    print(f'We have not found {to_find} in the list.')
