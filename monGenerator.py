from genMonster import Generic
from random import randint

class Goblin(Generic):
    def __init__(self):
        super().__init__("Goblin", 10, "Sword")

class Troll(Generic):
    def __init__(self):
        super().__init__("Troll", 10, "Club")

class Generator:
    def __init__(self):
        self.__choices = [Goblin, Troll]

    def create(self):
        return self.__choices[randint(0, 1)]
