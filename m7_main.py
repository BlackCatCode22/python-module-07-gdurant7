from ZooB import ZooB


animal_file = input('Enter File Name For Animals: ')  # animalsEdited.txt
name_file = input('Enter File Name For Names: ')      #namesEdited.txt
ZooA_instance = ZooB()
ZooA_instance.files(animal_file, name_file)
ZooB.write_report()