# Inheritance = pass atributes and methods to another class.
class Vehicle:
    def __init__(self):
        self.brand = 'Any'
class LandVehicle(Vehicle):
    def __init__(self):
        super().__init__()
class TrackedVehicle(LandVehicle):
    def __init__(self):
        super().__init__()

# Method issubclass(CLASS1, CLASS2) => True if CLASS2 is a subclass of CLASS1.
print(issubclass(Vehicle, Vehicle)) # => True, with itself
print(issubclass(Vehicle, LandVehicle)) # => False
print(issubclass(TrackedVehicle, Vehicle)) # => True

# Method isinstance(OBJ, CLASS) => True if OBJ belongs to CLASS.
my_vehicle = Vehicle()
print(isinstance(my_vehicle, Vehicle)) # => True
print(isinstance(my_vehicle, LandVehicle)) # => False

# Operator is => OBJ1 is OBJ2 => True if those two variables point to the same object.
my_vehicle2 = LandVehicle()
my_vehicle3 = TrackedVehicle()
print(my_vehicle2 is my_vehicle3) # => False

# Check difference with operator ==, which returns True if those two values are equal.
print(my_vehicle2.brand == my_vehicle3.brand) # => True, because both brand = 'Any', so if we change:
my_vehicle3.brand = 'Toyota'
print(my_vehicle2.brand == my_vehicle3.brand) # => False
