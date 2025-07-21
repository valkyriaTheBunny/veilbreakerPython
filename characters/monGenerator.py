from characters.genMonster import Generic
from equipment.weapons import Weapon
from random import choice

class Generator:
    def __init__(self):
        self.__choices = [
            lambda: Generic("Goblin", 10, Weapon("Dagger", 5), "green", 200),
            lambda: Generic("Troll", 10, Weapon("Club", 8), "aquamarine4", 280),
            lambda: Generic("Orc", 12, Weapon("Tree Branch", 12), "chocolate4", 275),
            lambda: Generic("Demon", 16, Weapon("Iron Sword", 15), "coral3", 195),

        ]

    def create(self, level: int):
        return choice(self.__choices[(level - 1):(level + 1)])()
