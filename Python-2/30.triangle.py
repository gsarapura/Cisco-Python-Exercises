import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    # Distance from another object;
    def distance_from_point(self, point):
            __x_distance = math.fabs(self.__x - point.getx())
            __y_distance = math.fabs(self.__y - point.gety())
            return math.hypot(__x_distance, __y_distance)
 
class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.__vertices = [vertex1, vertex2, vertex3]

    def perimeter(self):
        # Triangle has 0, 1 and 2 vertices.
        # To calculate perimiter => Perimeter = 0-1 + 1-2 + 2-0
        __distance1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        __distance2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        __distance3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return __distance1 + __distance2 + __distance3

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())