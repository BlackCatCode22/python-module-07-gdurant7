from ZooA import ZooA

class Hyena(ZooA):

    def hyena_sounds(self):
           sound = 'Make mine a "cub" sandwich!'
           return f'{self._species} says: {sound}'

class Lion(ZooA):

    def lion_sounds(self):
        sound = 'Remember who you are.'
        return f'{self._species} says: {sound}'

class Bear(ZooA):

    def bear_sounds(self):
        sound = 'Look for the BEAR necessities!'
        return f'{self._species} says: {sound}'

class Tiger(ZooA):

    def tiger_sounds(self):
        sound = "They're GR-R-REAT!"
        return f"{self._species} says: {sound}"