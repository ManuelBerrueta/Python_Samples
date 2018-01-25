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

lalo = Person("Jim", "negro", "7 ft")

send_it = Manuel.print_hair_color(), Manuel.print_height(), Manuel.print_name()

lalo.print_hair_color()
lalo.print_height()
lalo.print_name()

my_name = input("Who Are you?")

if my_name == "Manny":
    print % send_it
