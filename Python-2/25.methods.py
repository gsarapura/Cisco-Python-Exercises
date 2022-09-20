class Videogame():
    maps = []
    def __init__(self, category = 'None'): # A method must always have one parameter, by convention 'self'.
        if category == 'None':
            self.category = 'It is just a game.'
        else:
            self.category = category
    def add_map(self, maps = []):
        self.maps.append(maps)
    def positive_method(self):
        self.dou = 'Yas'
    def printing(self):
        print(self.category, self.maps, self.positive_method()) # 'self' is used to access to class and instance variables.
        # Also to access functions.
    def __hidden(self):
        print('I am hidden')
cs_go = Videogame('Shooter')
among_us = Videogame()

cs_go.add_map('Inferno')

cs_go.printing()
# among_us.__hidden() => AttributeError, to solve this:
among_us._Videogame__hidden()
# Method __name__ to get class name from classes. Method type() + __name__ to get class name from objects:
print(Videogame.__name__)
print(type(among_us).__name__)
# Method __module__  is intended for retrieving the module where the function was defined, either to read the source code or sometimes to re-import it in a script.
print(Videogame.__module__)
print(cs_go.__module__)