from genMonster import Generic
from random import choice

class Generator:
    def __init__(self):
        self.__choices = [
            lambda: Generic("Goblin", 10, "Sword"),
            lambda: Generic("Troll", 10, "Club")
        ]

    def create(self):
        return choice(self.__choices)()
