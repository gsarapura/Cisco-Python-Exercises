# Just a program that tells whether it is a leap or a common year.
# Some doubts: integers to string, possible bug?
# Note: would it be easier if I just print() on every branch?

year = int(input("Type a year:"))
# Can this create a bug? It then may changed to a string. I guess that's why Python is dynamically typed.
result = 0

if year > 1582:
    if year % 4 != 0:
        result = "Standard year."  # or print()?
    elif year % 100 != 0:
        result = "Leap year."
    elif year % 400 != 0:
        result = "Standard year."
    else:
        result = "Leap year."
else:
    print("It is not within the Gregorian Calendar.")

if result == "Standard year." or result == "Leap year.":
    print(result)
