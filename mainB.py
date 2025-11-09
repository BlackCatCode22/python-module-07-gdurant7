from datetime import datetime
import random
import ZooB

zooDictionary = {'hyena': [], 'lion': [], 'bear': [], 'tiger': []}

next_id = 101
arrival = datetime.today().strftime('%d-%m-%y')


name_list= list()
with open('animalNames.txt') as file:
    for line in fileNames:
        line = line.strip()
        if not (line.startswith('Hyena') or line.startswith('Lion')
                or line.startswith('Bear') or line.startswith('Tiger')):
            words = line.split(',')
            for words in words:
                name = words.strip()
                if words not in name_list: name_list.append(words)

    name = random.sample(name_list, 1)

with open('arrivingAnimals.txt') as fileAnimals:
    for line in fileAnimals:
        line = line.strip()
    parts = line.split(',')
    words = line.split()
    species = words[4]
    ids = species[0:3] + str(next_id)
    next_id += 1
    age = int(words[0])
    sex = words[3]

    if parts[1].split()[0] == 'unkown':
        season = 'unkown'
    else:
        season = parts[1].split()[-1]

    year = 2025 - age
    season = season.lower()
    day = str(21)
    if season == 'winter':
        month = 'JAN.'
    if season == 'spring':
        month = 'APR.'
    if season == 'summer':
        month = 'JUL.'
    if season == 'fall':
        month = 'NOV.'
    else:
        month = 'JAN.'
    date = [day, month, str(year)]
    birth_date = ' '.join(date)

    color = ' '.join(parts[2].split()[:-1])
    weight = parts[3]
    preOrigin = parts[-2].split()[1:]
    origin = ' '.join(preOrigin)
    place = words[-1]



    wordList = [species, ids, age, name, sex, birth_date, color, weight, origin, place, arrival]
    #print(wordList)
    print(species, ids, age, name, sex, birth_date, color, weight, origin, place, arrival)