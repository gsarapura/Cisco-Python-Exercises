import math

# Create a class that instantiates ponits on the Cartesian system.
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    # math.fabs() is for absolute value and math.hypot() is for hypotenuse calculation.
    def distance_from_xy(self, x, y):
        __x_distance = math.fabs(self.__x - x)
        __y_distance = math.fabs(self.__y - y)
        return math.hypot(__x_distance, __y_distance)
    # Calculate distance from another object:
    def distance_from_point(self, point):
        __x_distance = math.fabs(self.__x - point.getx())
        __y_distance = math.fabs(self.__y - point.gety())
        return math.hypot(__x_distance, __y_distance)

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point2.distance_from_xy(2, 0))
print(point2.distance_from_point(point1))