class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0):
        if hour < 10:
            self.__hour = '0' + str(hour)
        else:
            self.__hour = str(hour)
        if minute < 10:
            self.__minute = '0' + str(minute)
        else:
            self.__minute = str(minute)
        if second < 10:
            self.__second = '0' + str(second)
        else:
            self.__second = str(second)

    def __str__(self):
        return self.__hour + ':' + self.__minute + ':' + self.__second

    def next_second(self):
        self.__second = str(int(self.__second) + 1)

    def prev_second(self):
        self.__second = str(int(self.__second) - 1)

timer = Timer(23, 59, 30)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)