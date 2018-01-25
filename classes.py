class Person:

    def __init__(self, name, hair_color, height):
        self.name = name
        self.hair_color = hair_color
        self.height = height

    def print_name(self):
        print(self.name)

    def print_height(self):
        print(self.height)

    def print_hair_color(self):
        print(self.hair_color)

Manuel = Person("Manuel Berrueta", "brown", "6 ft")

Pompis = Person("El Papi", "negro", "7 ft")

Manuel.print_hair_color()
Manuel.print_height()
Manuel.print_name()

Pompis.print_hair_color()
Pompis.print_height()
Pompis.print_name()

