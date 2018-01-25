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

class Employee(Person):
    def __init__(self, employee_id):
        self.employee_id = employee_id




Manuel = Person("Manuel Berrueta", "brown", "6 ft")






