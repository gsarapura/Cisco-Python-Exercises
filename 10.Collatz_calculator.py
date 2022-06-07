# it shows the number of calculations made and the intermediate results.

steps = 0
number = int(input("Type in a number: "))

while number != 1:
    if number % 2:
        number = number * 3 + 1
        steps += 1
        print(number)
    else:
        number //= 2
        steps += 1
        print(number)
print("Steps taken:", steps)
