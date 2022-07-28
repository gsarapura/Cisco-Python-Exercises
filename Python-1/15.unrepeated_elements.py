# Create empty list:
my_list = []

# Ask for list's length:
list_range = int(input("Type in the range of the list: "))

# Ask for numbers:
for i in range(list_range):
    number = int(input("Type in integers you want: "))
    my_list.append(number)
print(my_list)

# Delete repeated elements by creating a new list:
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

# Print the new list
print("List without repeated elements:")
print(new_list)
