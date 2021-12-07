# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_vehicle = Vehicle(90, 100)


# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seat_capacity(self):
        print(f"Bus has {self.capacity} seats.")


my_bus = Bus(90, 110, 45)

# 3
print(type(my_bus))

# 4
School_bus = Bus(100, 110, 50)
print(isinstance(School_bus, Vehicle))


# 5
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students


# 6
class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, capacity)
        self.bus_school_color = bus_school_color

    def bus_school_color(self):
        print(f'Color of this bus is {self.bus_school_color}.')


my_schoolBus = SchoolBus(25, 300, 100, 110, 50, "yellow")
print(my_schoolBus.bus_school_color)


# 7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"Bear makes sound {self.sound}")


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"Wolf makes sound {self.sound}")


bear = Bear("Grraaau")
wolf = Wolf("Auuuuuf")

animals = (bear, wolf)
for animal in animals:
    print(animal.make_sound())


# 8
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def check(self):
        if self.population > 1500:
            return self.population
        else:
            print(f"{self.name} is so small city")


Lviv = City('Lviv', 25000)
Holovetske = City('Holovetske', 1000)
Rivne = City('Rivne', 20000)

cities = (Lviv, Holovetske, Rivne)

for i in cities:
    print(i.check())