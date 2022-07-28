# Print the largest number (boolean version).

# I get the break statement, looks pretty useful.
flag_largest = True
counter = 0

while True:
    number = int(input("Type in a number or -1 to finish the program: "))
    if number == -1:
        break

    counter += 1

    if flag_largest:
        largest_number = number
        flag_largest = False

    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is " + str(largest_number) + ".")
else:
    print("You haven't type in any number.")
