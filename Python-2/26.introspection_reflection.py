class Vehicles():
    def __init__(self, brand = 'None', color = 'None'):
        self.brand = brand
        self.color = color

car = Vehicles('Fiat', 'Red')

# print(car.__dict__.keys()) => dict_keys(['brand', 'color'])
# getattr(CLASS, KEY) => print(getattr(car, 'brand')) => Fiat
# isinstance(VALUE, DATATYPE) => print(isinstance(getattr(car, 'number'), int)) => True
# setattr(OBJ, KEY, VALUE) => setattr(car, 'number', getattr(car, 'number') + 1 )

car.number = 2
print('Before adding:', car.__dict__)

def incIntsN(obj):
    """Add 1 to attributes starting with 'n' and containing int values."""
    # Iterate over object dictionary to get keys:
    for name in obj.__dict__.keys(): 
        # Check whether the key starts with 'n':
        if name.startswith('n'):
            val = getattr(obj, name)
            # Check whether the values is an integer:
            if isinstance(val, int): 
                # Add 1 to attribute:
                setattr(obj, name, val + 1)
                
incIntsN(car)
print('After adding:', car.__dict__)