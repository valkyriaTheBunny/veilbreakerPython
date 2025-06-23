from genMonster import Generic
from random import randint

Goblin = Generic("Goblin", 10, "Sword")
Troll = Generic("Troll", 10, "Club")

class Generator:
    def __init__(self):
        self.__choices = [Goblin, Troll]

    def create(self):
        return self.__choices[randint(0, 1)]
