from random import randrange
from random import randint
from datetime import datetime
import pygame, random

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.monList = []
        self.__grid = []
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

    def show(self, surf):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "wall":
                    pygame.draw.rect(surf, "purple", (i * 50, j * 50, 50, 50))
                else:
                    pygame.draw.rect(surf, "gold", (i * 50, j * 50, 50, 50))

    def checkPos(self):
        pass
