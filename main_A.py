rom ZooA import ZooA


animal_file = input('Enter File Name For Animals: ')  # animalsEdited.txt
name_file = input('Enter File Name For Names: ')      #namesEdited.txt
ZooA_instance = ZooA()
ZooA_instance.files(animal_file, name_file)
ZooA.write_report()

