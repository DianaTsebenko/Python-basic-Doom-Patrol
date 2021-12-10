import dataclasses
from collections import namedtuple


# 1.
class Laptop:
    def __init__(self):
        battery = Battery('This is energy of laptop')
        self.battery = battery


class Battery:
    def __init__(self, energy):
        self.energy = energy


laptop = Laptop()
print(laptop.battery.energy)


# 2
class Guitar:
    def __init__(self, strings):
        self.strings = strings


class GuitarString:
    def __init__(self):
        pass


string = GuitarString()
guitar = Guitar(string)


# 3
class Calc:
    @staticmethod
    def add_nums(num_1, num_2, num_3):
        return num_1 + num_2 + num_3


calc = Calc()
print(calc.add_nums(40, 11, 23))


# 4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


Pasta_carb = Pasta.carbonara()
Pasta_bol = Pasta.bolognaise()
print(Pasta_carb)
print(Pasta_bol)


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count):
        self.visitors_count = 0

    @property
    def visit_count(self):
        return self.visitors_count

    @visit_count.setter
    def visit_count(self, num):
        if num > self.max_visitors_num:
            self.visitors_count = self.max_visitors_num


Concert.max_visitor_num = 50
concert = Concert(1000)
concert.visitors_count = 1000
print(concert.visitors_count)


# 6
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(key=13,
                                    name='Diana',
                                    phone_number='098-205-09-03',
                                    address='Street No Name 2',
                                    email='dianats@gmail.com',
                                    birthday='sixth of July',
                                    age=16)

print(address_book)

# 7
AddressTuple = namedtuple('AddressBookDataClass',
                          ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

address_book_tuple = AddressTuple(28, 'Ann', '097-476-43-12', 'Cool', 'name@gmail.com', '18.11.2000', 21)
print(address_book_tuple)


# 8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return (f'AddressBook(key={self.key}, name={self.name}, '
                f'phone_number={self.phone_number}, address={self.address},'
                f'email={self.email}, birthday={self.birthday}, '
                f'age={self.age})')


address_book_1 = AddressBook(key=12,
                             name='OLeg',
                             phone_number='098-344-45-08',
                             address='Street Happy',
                             email='olegclo@gmail.com',
                             birthday='09.12.1999',
                             age=22)
print(address_book_1)


# 9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.county = country

    @property
    def print_age(self):
        return f'It is {self.name}, and he is {self.age} years old'


person = Person('John', 36, 'USA')
print(person.print_age)
person.age = 39
print(person.print_age)


# 10
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(2347, "Diana")
setattr(student, 'st_email', 'ditseb@i.o')
print(getattr(student, 'st_email'))


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def print_temperature(self):
        return self._temperature

    @print_temperature.setter
    def temperature(self, new_t):
        self._temperature = new_t


f_temperature = Celsius(10)
f_temperature.temperature = f_temperature.temperature * 1.8 + 32
print(f_temperature.temperature)
