# Class Weeker that instantiates days of the week.
class WeekDayError(Exception):
    pass
	
class Weeker:
    # Create list of days:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        # If input is not in the list, raise WeekDayError-
        try:
            self.__current_index = Weeker.__days.index(day)
        except ValueError:
            raise WeekDayError
    def __str__(self):
        return Weeker.__days[self.__current_index]
    def add_days(self, n):
        self.__current_index = (self.__current_index + n) % 7 # I can't exaplain this
    def subtract_days(self, n):
        self.__current_index = (self.__current_index - n) % 7  # I can't exaplain this
        
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")