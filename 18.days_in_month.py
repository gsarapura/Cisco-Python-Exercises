
# Given year and month, print the number of days a month has. Remember February in leap years.

def is_year_leap(year):
    assert year > 1582, "Year is not within the Gregorian Calendar."
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    assert month >= 0 and month <=11, 'Month is out of range'
    if is_year_leap(year):
        days_in_month[1] = 29
    return days_in_month[month - 1]

def input_output():
    months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octub", "November", "December"]
   
    month = int(input("Type in the month: "))
    year = int(input("Type in the year: "))

    days_in_m = days_in_month(year, month)

    print(f'For the year {year}, {months_names[month -1]} has {days_in_m} days.')

input_output()
