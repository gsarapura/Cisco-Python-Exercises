#Finding a number in the list.

lista_one = [2, 3, 4, 5, 6]
to_find = int(input("Type in the number you are looking for: "))
found = False

for i in range(len(lista_one)):
    found = lista_one[i] == to_find
    if found:
        break
if found:
    print(f'We have found {to_find} in the list.')
else:
    print(f'We have not found {to_find} in the list.')
