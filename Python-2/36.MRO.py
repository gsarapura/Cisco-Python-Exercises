# Method Resolution Order(MRO) 
# 1. The method or attribute is searched within the class.
# 2. The order in which the classes are inherited => From right to left.
class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Bottom(Middle_Left, Middle_Right): # It will print 'middle-left', if we interchange them => 'middle-right'
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom() # => bottom
object.m_middle() # => middle_left
object.m_top() # => top