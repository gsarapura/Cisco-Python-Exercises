# Doubt about continue statement

counter = 0

number = int(input("Type in a number or -1 to finish the program: "))
largest_number = number

while number != -1:
    # if number == -1: WHY use this when the program executes regardless?
    #     continue

    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Type in a number or -1 to finish the program: "))

if counter:
    print("The largest number is " + str(largest_number) + ".")
else:
    print("You haven't typed in any number.")
