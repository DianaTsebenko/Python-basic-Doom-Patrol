import time
import random
import uuid
from abc import ABC, abstractmethod


class Animal:
    types = ("Herbivores", "Predator")

    def __init__(self, power, speed):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.is_out_of_power = False

    def eat(self, power):
        self.current_power += power
        if self.current_power + power >= self.max_power:
            self.current_power = self.max_power

    def lose_power(self, power):
        self.current_power -= power
        if self.current_power <= 0:
            self.is_out_of_power = True

    @abstractmethod
    def get_name(self):
        pass

    def get_animal_info(self):
        return self.get_name() + "  " + str(self.id)


class Predator(Animal):
    def get_name(self):
        predator = ["Wolf", "Bear", "Fox", "Boar"]
        return random.choice(predator)


class Herbivorous(Animal):
    def get_name(self):
        herbivore = ["Rabbit", "Dear", "Squirrel", "Beaver"]
        return random.choice(herbivore)


class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def animal_id(self, hunter_id=None):
        if not isinstance(hunter_id, type(None)):
            key_list = list(key for key in self.animals.keys()
                            if key != hunter_id)
        else:
            key_list = list(self.animals.keys())

        animal_key = random.choice(key_list)
        return self.animals[animal_key]

    def get_animals_count(self):  # get count of animals in Forest
        return len(self.animals)

    def stop(self):
        if self.get_animals_count() <= 1:
            return False
        return True

    @staticmethod
    def animal_list():
        for animal in my_forest.animals.keys():
            print(my_forest.animals[animal].get_animal_info())

    @staticmethod
    def animal_generator():
        animal_type = random.choice(Animal.types)

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal

    def any_predator_left(self):
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True

        return False

    def hunting(self):
        hunter = Forest.animal_id(self)

        if isinstance(hunter, Herbivorous):
            hunter.eat(50)

        victim = Forest.animal_id(self, hunter.id)

        if hunter.speed > victim.speed and \
                hunter.current_power > victim.current_power:
            hunter.eat(50)
            victim.is_out_of_power = True
        else:
            hunter.lose_power(30)
            victim.lose_power(30)

        if hunter.is_out_of_power:
            self.remove_animal(hunter)

        if victim.is_out_of_power:
            self.remove_animal(victim)


if __name__ == "__main__":

    Forest.animal_generator()
    my_forest = Forest()

    for i in range(10):
        animal = Forest.animal_generator()
        my_forest.add_animal(animal)

    print("Forest list >>>")
    my_forest.animal_list()

    print("It's hunting time!")

    time.sleep(4)

    while my_forest.any_predator_left() and my_forest.stop:
        my_forest.hunting()

    print("Who survived in the forest >>>")
    my_forest.animal_list()
