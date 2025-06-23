from random import randint
from datetime import datetime
from monGenerator import Generator
import pygame, random

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.__monList = []
        self.__grid = []
        self.__gen = Generator()
        ms = datetime.time(datetime.now()).microsecond
        random.seed(ms * 100000)

    def __genNoise(self):
        noiseDen = 65
        for i in range(self.__width):
            self.__grid.append([])
            for _ in range(self.__height):
                gen = randint(-1, 101)
                if gen >= noiseDen:
                    self.__grid[i].append("wall")
                else:
                    self.__grid[i].append("floor")

    def __smoothing(self):
        for _ in range(500):
            temp = self.__grid
            for j in range(self.__width):
                for k in range(self.__height):
                    nWallCnt = self.__wallCount(temp, j, k)

                    r = randint(1, 5)
                    if nWallCnt > r:
                        self.__grid[j][k] = "wall"
                    else:
                        self.__grid[j][k] = "floor"

    def __wallCount(self, temp, inX, inY):
        cnt = 2
        for i in range(inX - 1, inX + 1):
            for j in range(inY - 1, inY + 1):
                if ((i > 0 and j > 0 ) and
                    (i < self.__width and j < self.__height)):

                    if i != inX and j != inY:
                        if temp[i][j] == "wall":
                            cnt += 1
                else:
                    cnt += 1
        return cnt

    def genRoom(self):
        self.__genNoise()
        self.__smoothing()
        self.__genMonsters()

    def __genMonsters(self):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "floor" and randint(0, 100) > 55:
                    mon = self.__gen.create()
                    mon.setPos(i, j)
                    self.__monList.append(mon)


    def show(self, surf):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "wall":
                    pygame.draw.rect(surf, "purple", (i * 50, j * 50, 50, 50))
                else:
                    pygame.draw.rect(surf, "gold", (i * 50, j * 50, 50, 50))

        for mon in self.__monList:
            mon.show(surf)

    def update(self, target):
        for mon in self.__monList:
            mon.move(target, self)

    def sPos(self):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.checkPos(i, j):
                    return [i, j]

    def checkPos(self, x, y):
        if x < 0 or y < 0 or x > self.__height or y > self.__width:
            return False
        return self.__grid[x][y] == "floor"
