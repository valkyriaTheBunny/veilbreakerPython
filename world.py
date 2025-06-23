from random import randrange

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.monList = []
        self.grid = []

    def __genNoise(self):
        noiseDen = 55
        for i in range(self.__width):
            self.grid[i] = []
            for j in range(self.__height):
                gen = randrange(0, 100)
                if gen > noiseDen:
                    self.grid[i][j] = "floor"
                else:
                    self.grid[i][j] = "wall"

    def __smoothing(self):
        for i in range(75):
            temp = self.grid
            for j in range(self.__width):
                for k in range(self.__height):
                    nWallCnt = 0
                    pass
