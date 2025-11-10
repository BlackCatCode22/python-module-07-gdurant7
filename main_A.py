import ZooSubSounds
from ZooA import ZooA
from ZooSubSounds import hyena, lion, bear, tiger


animal_file = input('Enter File Name For Animals: ')
name_file = input('Enter File Name For Names: ')
ZooA_instance = ZooA(0, 'a', 'b', 0, 'c', 'd', 'e', 'f', 'g'  )
ZooA_instance.files(animal_file)
ZooA_instance.name_generator(name_file)
ZooA.write_report()

print("\n-----Example of Zoo Sounds-----\n")
print(ZooSubSounds.hyena(0, 'a', 'b', 0, 'c', 'd', 'e', 'f', 'g' ))
print(ZooSubSounds.lion(0, 'a', 'b', 0, 'c', 'd', 'e', 'f', 'g' ))
print(ZooSubSounds.bear(0, 'a', 'b', 0, 'c', 'd', 'e', 'f', 'g' ))
print(ZooSubSounds.tiger(0, 'a', 'b', 0, 'c', 'd', 'e', 'f', 'g' ))
