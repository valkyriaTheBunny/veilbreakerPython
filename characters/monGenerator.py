from characters.genMonster import Generic
from random import choice

class Generator:
    def __init__(self):
        self.__choices = [
            lambda: Generic("Goblin", 10, "Dagger", "green"),
            lambda: Generic("Troll", 10, "Club", "aquamarine4"),
            lambda: Generic("Orc", 12, "Tree Branch", "chocolate4"),
            lambda: Generic("Demon", 16, "Iron Sword", "coral3"),

        ]

    def create(self, level: int):
        return choice(self.__choices[(level - 1):(level + 1)])()
