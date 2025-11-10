from datetime import datetime
import random

class ZooA:

    animal_count = 0 #keeps count of how many animal objects.
    animal_id = 101 #used to create unique ID for animals.

    #universal dictionary lists to hold animal information.
    animals = {'hyena':[], 'lion':[], 'tiger':[], 'bear':[]}

    def __init__(self, age, sex, species, date_birth, color, weight, came_from, habitat,
                 name):
        date_arrival = datetime.today().strftime('%d-%m-%y')
        self._age = age
        self._sex = sex
        self._species = species.lower()
        self._date_birth = date_birth
        self._color = color
        self._weight = weight
        self._came_from = came_from
        self._habitat = habitat
        self._name = name
        animal_id = f'{self._species[:3]}{ZooA.animal_id}'
        ZooA.animal_count += 1
        ZooA.animal_id += 1

        animal_info = {
            'ID': animal_id,
            'Name': name,
            'Sex': self._sex,
            'Date of Birth': self._date_birth,
            'Color': self._color,
            'Sent From': self._came_from,
            'Habitat': self._habitat,
            'Arrived On': date_arrival}

        if self._species in ZooA.animals:
            ZooA.animals[self._species].append(animal_info)
        else:
            print(f'UNKNOWN SPECIES: {self._species}')
    
    @staticmethod
    def string_to_tuple(animal_string):
        age, sex, species, season, color, weight, came_from, habitat = animal_string.split()
        return int(age), str(sex), str(species), str(season), str(color), int(weight), str(came_from), str(habitat)

    @staticmethod
    def tuple_to_string(animal_tuple):
        animal_string = ' '.join(map(str, animal_tuple))  #step 2: now send to string_to_tuple to split, and assign value.
        return animal_string


    def files(self, animal_file, name_file):
        animal_data = []
        name = []
        try:
            with open(animal_file, 'r') as file1:
                lines = file1.readlines()
                animal_tuple = [ZooA.string_to_tuple(line.strip()) for line in lines]   #step 1: send to string_to_tuple to ensure uniformity
                animal_data.extend(animal_tuple)
            with open(name_file, 'r') as file:
                for line in file:
                    name.append(line.strip())
            random.shuffle(name)
            for data, animal_name in zip(animal_data, name):
                age, sex, species, season, color, weight, came_from, habitat = data
                date_birth = ZooA.date_birth(age, season)
                ZooA(age, sex, species, date_birth, color, weight, came_from, habitat, animal_name)
            return animal_data, name
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            print('Please check file name and try again.')

    @staticmethod
    def date_birth(age, season):
        day = 21
        year = datetime.now().year - age
        month = season
        if month == 'winter':
            month = 'JAN'
        elif month == 'spring':
            month = 'APR'
        elif month == 'summer':
            month = 'JUL'
        elif month == 'fall':
            month = 'NOV'
        else: month = 'JAN'
        date_birth = f'{year}-{month}-{day}'
        return date_birth

    @staticmethod
    def write_report():
        date_arrival = datetime.today().strftime('%d-%m-%y')
        with open('zooPopulation.txt', 'w') as output:
            output.write(' ZOO POPULATION REPORT '.center(100, '=') + '\n\n')

            output.write(f'Number of Animals: {ZooA.animal_count}\n')
            output.write(f'Arrival Date: {date_arrival}\n\n')

            output.write(' HYENA HABITAT '.center(100, '-') + '\n\n')
            for hyena_value in ZooA.animals['hyena']:
                output.write(str(hyena_value) + '\n')
            output.write('\n\n')

            output.write(' LION HABITAT '.center(100, '-') + '\n\n')
            for lion_value in ZooA.animals['lion']:
                output.write(str(lion_value) + '\n')
            output.write('\n\n')

            output.write(' BEAR HABITAT '.center(100, '-') + '\n\n')
            for bear_value in ZooA.animals['bear']:
                output.write(str(bear_value) + '\n')
            output.write('\n\n')

            output.write(' TIGER HABITAT '.center(100, '-') + '\n\n')
            for tiger_value in ZooA.animals['tiger']:
                output.write(str(tiger_value) + '\n')
            output.write('\n\n')

            output.write(''.center(100, '='))
            output.write(' END OF REPORT '.center(100))
            output.write(''.center(100, '='))
            output.close()

        new_file = open('zooPopulation.txt', 'r')
        file_contents = new_file.read()
        print(file_contents)
