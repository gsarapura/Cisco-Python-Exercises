# Ask for a list of years and then check whether or not they are leap years.

def list_input():
    new_list = []
    list_range = int(input("Type in quantity of years: "))
    for i in range(list_range):
        element = int(input("Type in years: "))
        new_list.append(element)
    return new_list

def is_year_leap(year):
    assert year > 1582, "Year is not within the Gregorian Calendar." # Test. Try/except difference?
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def check_list_year():
    list_year = list_input()
    for i in list_year:
        if is_year_leap(i):
            print(f'{i} is leap year.')
        else:
            print(f'{i} is not leap year.')

check_list_year()