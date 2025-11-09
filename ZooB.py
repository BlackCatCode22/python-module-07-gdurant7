from datetime import datetime

class Zoo:

    animalCount = 0

    def __init__(self, species, id, name, age, sex, birth_date, color, weight, origin, place, arrival):
        self.species = species
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.birth_date = birth_date
        self.color = color
        self.weight = weight
        self.origin = origin
        self.place = place
        self.arrival = arrival
        Zoo.animalCount += 1



class Hyena(Zoo):

    def add_sounds(self, sounds):
        self.sounds.append(sounds)

class Lion(Zoo):

    def add_sounds(self, sounds):
        self.sounds.append(sounds)

class Bear(Zoo):

    def add_sounds(self, sounds):
        self.sounds.append(sounds)

class Tiger(Zoo):

    def add_sounds(self, sounds):
        self.sounds.append(sounds)