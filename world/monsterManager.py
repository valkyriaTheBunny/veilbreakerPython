from characters.monGenerator import Generator
from random import randint
from datetime import datetime
import random

class Manager:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.__monList = []
        self.__generator = Generator()
        ms = datetime.time(datetime.now()).microsecond
        random.seed(ms * 500000 + ms ** 2)

    def genMons(self, map: list[list[int]], level: int):
        #randomly generates monster starting positions
        for i in range(self.__width):
            for j in range(self.__height):
                if map[i][j] == "floor" and randint(40, 1000) < 55:
                    #generates a random monster class instance
                    #marking its initially position as occupied so that
                    #multiple monsters cannot spawn on the same square

                    mon = self.__generator.create(level)
                    mon.setPos(i, j)
                    map[i][j] = "occupied"
                    self.__monList.append(mon)

        return self.__monList

    def update(self, world, player, dt):
        #updates the world, specifically monsters in the world
        #needs dt so that monsters can move independent of the player
        #and player so that monsters can attack the player
        for i, mon in enumerate(self.__monList):
            if mon.health <= 0:
                self.__monList.pop(i)
            else:
                mon.move(world, player, dt)

    def isAttackable(self, map: list[list[int]], x: int, y: int, atkVal: int):
        #returns a monster if there is a monster at a given grid location
        #or false if there is no monster
        for i, mon in enumerate(self.__monList):
            if mon.getPos() == (x, y) and mon.health <= atkVal:
                self.__monList.pop(i)
                map[x][y] = "floor"
            elif mon.getPos() == (x, y):
                return mon
        return False
