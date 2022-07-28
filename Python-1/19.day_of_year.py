# Given year, month and day determine which day of the year it is: 1-365/366

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
    
    assert month >= 0 and month <=12, "Month is out of range"

    if is_year_leap(year):
        days_in_month[1] = 29
    
    return days_in_month[month - 1] # Month 1 corresponds to index 0 in the "days_in_month" list.

# Check the day of the year (1-365/366)
def day_of_year(year, month, day):
    assert day > 0, "Day of year is out of range"
    if not is_year_leap(year) and month == 2: # Any improvement fo the testing?
        assert day < 29, "It is not a leap year"

    day_of_year = 0

    if month == 1: # If it is January, then "day" equals to the day of the year.
        return day
    else:
        for i in range(month - 1): # Loop that counts the days before the month in the input/test data.
            day_of_year += days_in_month(year, i + 1) # Staring i equals to 0. See days_in_month function.
    day_of_year += day # Add the days of the month in the input/test data.

    return day_of_year 

def input_output():
    months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octub", "November", "December"]
   
    year = int(input("Type in the year: "))
    month = int(input("Type in the number of the month: "))
    day = int(input("Type in the day: "))

    number_of_day = day_of_year(year, month, day)

    print(f"For the date {year}.{month}.{day}, it is the day number {number_of_day}.")

input_output()
