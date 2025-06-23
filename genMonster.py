import pygame

class Generic:
    def __init__(self, name, health, equip):
        self.name = name
        self.health = health
        self.equip = equip
        self.__x = 0
        self.__y = 0


    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getPos(self):
        return (self.__x, self.__y)

    def move(self, world):
        for i in range(self.__x - 1, self.__x + 1):
            for j in range(self.__y - 1, self.__y + 1):
                if ((i, j) != self.getPos()) and world.checkPos(i, j):
                    print(i, j)
                    self.setPos(i, j)
                    break

    def show(self, surf):
        pygame.draw.rect(surf, "green", (self.__x * 50, self.__y * 50, 50, 50))
