from random import randrange
from random import randint
import pygame

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.monList = []
        self.__grid = []

    def __genNoise(self):
        noiseDen = 55
        for i in range(self.__width):
            self.__grid[i] = []
            for j in range(self.__height):
                gen = randrange(0, 100)
                if gen > noiseDen:
                    self.__grid[i][j] = "floor"
                else:
                    self.__grid[i][j] = "wall"

    def __smoothing(self):
        for i in range(75):
            temp = self.__grid
            for j in range(self.__width):
                for k in range(self.__height):
                    nWallCnt = self.__wallCount(temp, j, k)

                    r = randint(2, 4)
                    if nWallCnt > r:
                        self.__grid[j][k] = "wall"
                    else:
                        self.__grid[j][k] = "floor"

    def __wallCount(self, temp, inX, inY):
        cnt = 0
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
