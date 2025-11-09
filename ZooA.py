from datetime import datetime

class ZooA:

    animal_count = 0 #keeps count of how many animal objects.
    animal_id = 101 #used to create unique ID for animals.

    #universal dictionary lists to hold animal information.
    animals = {'hyena':[], 'lion':[], 'tiger':[], 'bear':[]}

    animal_file = input('Enter File Name For Animals: ')
    name_file = input('Enter File Name For Names: ')

    def __init__(self, age, sex, species, date_birth, color, weight, came_from, habitat,
                 name):
        date_arrival = datetime.today().strftime('%d-%m-%y')
        self._age = age
        self._sex = sex
        self._species = species
        self._date_birth = date_birth
        self._color = color
        self._weight = weight
        self._came_from = came_from
        self._habitat = habitat
        animal_id = f'{self._species[:3]}{ZooA.animal_id}'
        ZooA.animal_count += 1
        ZooA.animal_id += 1

        #assign info so it can be sorted into lists
        animal_info = {
            'ID': animal_id,
            'Name': name,
            'Sex': self._sex,
            'Date of Birth': self._date_birth,
            'Color': self._color,
            'Sent From': self._came_from,
            'Habitat': self._habitat,
            'Arrived On': date_arrival
        }

        #sort by specis and append to list
        #tried if/elif, but noticed this when reading about f-strings
        if self._species in ZooA.animals:
            ZooA.animals[self._species].append(animal_info)
        else:
            print(f'UNKNOWN SPECIES: {self._species}')


    #function to convert string into a tuple and assign value to each part.
    #currently only takes CSV files, but will try including other formats.
    @staticmethod
    def string_to_tuple(animal_string):
        age, sex, species, season, color, weight, came_from, habitat = [x.strip() for x in animal_string.split(',')]
        return int(age), sex, species, season, color, int(weight), came_from, habitat

    #function to combining multiple strings or tuples into one string.
    #maybe send animal_line directly to tuple?
    @staticmethod
    def tuple_to_string(animal_tuple):
        animal_string = ' '.join(map(str, animal_tuple))  #step 2: now send to string_to_tuple to split, and assign value.
        return animal_string

    #function to import, open, read, and sparse files.
    @classmethod
    def import_files(cls, animal_file, name_file):
        animals = []
        name = []
        while True:
            try:
                with open(animal_file, 'r') as file:
                    for line in file:
                        animal_tuple = cls.string_to_tuple(line)  #step 1: send to string_to_tuple to ensure uniformity
                        animals.append(animal_tuple)
                        for animal_tuple, name in zip(animal_tuple, name_file):
                            age, sex, species, season, color, weight, came_from, habitat = animal_tuple
                            dob = ZooA.date_birth(age, season)
                            ZooA(age, sex, species, dob, color, weight, came_from, habitat, name)
                with open(name_file, 'r') as file:
                    for line in file:
                        name =  [n.strip() for n in line.split(',')]
                        animals.append(name)
                return animals, name
            except FileNotFoundError as e:
                print(f'File Not Found: {e}')
                print('Please check file name and try again.')

    #convert season to a month and concatenate into a date of birth.
    @staticmethod
    def date_birth(age, season):
        day = 21
        year = 2025 - age
        month = season.lower()
        if month == 'winter':
            month = 'JAN'
        elif month == 'spring':
            month = 'APR'
        elif month == 'summer':
            month = 'JUL'
        elif month == 'fall':
            month = 'NOV'
        else: month = 'JAN'



        season = season.lower()
        month_map = {'winter': 'JAN', 'spring': 'APR', 'summer': 'JUL', 'fall': 'NOV'}
        month = month_map.get(season, 'JAN')
        return f"{day}-{month}-{year}"

    #created to deal with TypError issues from animal_id returning (type NoneType).
    def __str__(self):
        date_arrival = datetime.today().strftime('%d-%m-%y')
        with open('zooPopulation.txt', 'w') as output:
            output.write(' ZOO POPULATION REPORT '.center(100, '=') + '\n\n')

            output.write(f'Number of Animals: {ZooA.animal_count}\n')
            output.write(f'Arrival Date: {date_arrival}\n\n')

            output.write(' HYENA HABITAT '.center(100, '-') + '\n\n')
            for hyena_value in ZooA.animals['hyena']:
                output.write(str(hyena_value) + '\n')
            output.write('\n')

            output.write(' LION HABITAT '.center(100, '-') + '\n\n')
            for lion_value in ZooA.animals['lion']:
                output.write(str(lion_value) + '\n')
            output.write('\n')

            output.write(' BEAR HABITAT '.center(100, '-') + '\n\n')
            for bear_value in ZooA.animals['bear']:
                output.write(str(bear_value) + '\n')
            output.write('\n')

            output.write(' TIGER HABITAT '.center(100, '-') + '\n\n')
            for tiger_value in ZooA.animals['tiger']:
                output.write(str(tiger_value) + '\n')
            output.write('\n\n\n\n\n')

            output.write(''.center(100, '='))
            output.write(' END OF REPORT '.center(100))
            output.write(''.center(100, '='))

        return f'{self._species[:3]}{ZooA.animal_id}'

