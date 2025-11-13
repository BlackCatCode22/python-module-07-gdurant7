from datetime import datetime
import random


class ZooB:
    animal_count = 0  # keeps count of how many animal objects.
    animal_id = 101  # used to create unique ID for animals.

    # universal dictionary lists to hold animal information.
    animals = {'hyena': [], 'lion': [], 'tiger': [], 'bear': []}

    def __init__(self):
        pass

    def add_animal(self, age, sex, species, date_birth, color, weight, came_from, habitat,
                   name):

        animal_id = f'{species[:3]}{ZooB.animal_id}'
        species = species.lower()
        date_arrival = datetime.today().strftime('%d-%m-%y')
        ZooB.animal_count += 1
        ZooB.animal_id += 1

        animal_info = {
            'Species': species,
            'ID': animal_id,
            'Name': name,
            'Age': age,
            'Sex': sex,
            'Date of Birth': date_birth,
            'Weight': weight,
            'Color': color,
            'Sent From': came_from,
            'Habitat': habitat,
            'Arrived On': date_arrival
        }

        if species in ZooB.animals:
            ZooB.animals[species].append(animal_info)
        else:
            print(f'UNKNOWN SPECIES: {species}')  # move init items to here for manually adding animals
            pass

    @staticmethod
    def string_to_tuple(animal_string):
        parts = animal_string.split(', ')
        p1 = parts[0].split()
        age = int(p1[0])
        sex = p1[3]
        species = p1[4]
        season_part = parts[1]
        if 'born in ' in season_part:
            season = season_part.split('born in ')[1]
        else:
            season = season_part
        color_full = parts[2]
        color = color_full.split(' color')[0]
        weight = parts[3]
        came_from = parts[4].split('from ')[1]
        habitat = parts[5]

        return age, sex, species, season, color, weight, came_from, habitat

    @staticmethod
    def tuple_to_string(animal_tuple):
        animal_string = ' '.join(
            map(str, animal_tuple))  # step 2: now send to string_to_tuple to split, and assign value.
        return animal_string

    def files(self, animal_file, name_file):
        animal_data = []
        name_list = []
        try:
            with open(animal_file, 'r') as file1:
                lines = file1.readlines()
                animal_tuple = [ZooB.string_to_tuple(line.strip()) for line in lines]
                animal_data.extend(animal_tuple)
            with open(name_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and ':' not in line:
                        temp = [i.strip() for i in line.split(',')]
                        name_list.extend([name for name in temp if name])
            random.shuffle(name_list)
            for data, animal_name in zip(animal_data, name_list):
                age, sex, species, season, color, weight, came_from, habitat = data
                date_birth = ZooB.birthday(age, season)
                self.add_animal(age, sex, species, date_birth, color, weight, came_from, habitat, animal_name)
            return animal_data, name_list
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            print('Please check file name and try again.')


    @staticmethod
    def birthday(age, season):
        day = 21
        year = datetime.now().year - age
        month = season.upper()
        if month == 'WINTER':
            month = 'JAN'
        elif month == 'SPRING':
            month = 'APR'
        elif month == 'SUMMER':
            month = 'JUL'
        elif month == 'FALL':
            month = 'NOV'
        else:
            month = 'JAN'
        date_birth = f'{year}-{month}-{day}'
        return date_birth

    @staticmethod
    def write_report():
        date_arrival = datetime.today().strftime('%d-%m-%y')
        with open('zooPopulation.txt', 'w') as output:
            output.write(' ZOO POPULATION REPORT '.center(100, '=') + '\n\n')

            output.write(f'Number of Animals: {ZooB.animal_count}\n')
            output.write(f'Arrival Date: {date_arrival}\n\n')

            output.write(' HYENA HABITAT '.center(100, '-') + '\n\n')
            for hyena_value in ZooB.animals['hyena']:
                output.write(str(hyena_value) + '\n')
            output.write('\n\n')

            output.write(' LION HABITAT '.center(100, '-') + '\n\n')
            for lion_value in ZooB.animals['lion']:
                output.write(str(lion_value) + '\n')
            output.write('\n\n')

            output.write(' BEAR HABITAT '.center(100, '-') + '\n\n')
            for bear_value in ZooB.animals['bear']:
                output.write(str(bear_value) + '\n')
            output.write('\n\n')

            output.write(' TIGER HABITAT '.center(100, '-') + '\n\n')
            for tiger_value in ZooB.animals['tiger']:
                output.write(str(tiger_value) + '\n')
            output.write('\n\n')

            output.write(' END OF REPORT '.center(100, '='))