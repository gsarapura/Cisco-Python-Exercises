# Python first checks indside objects, then superclasses.
# Overriding attributes and methods:
class Level1:
    var = 'In level 1'
    def fun(self):
        return 'Funny level 1'
class Level2(Level1):
    var = 'In level 2'
    def fun(self):
        return 'Funny level 2'
class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun()) # => In level 2 Funny level 2

# For multiple inheritance => Objects, then superclasses from left to right:
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"
class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"
class Sub(Right, Left):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun()) # => L LL RR Left // IF Sub(Right, Left) => R LL RR Right