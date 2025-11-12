rom ZooA import ZooA


animal_file = input('Enter File Name For Animals: ')
name_file = input('Enter File Name For Names: ')
ZooA_instance = ZooA()
ZooA_instance.files(animal_file, name_file)
ZooA.write_report()
