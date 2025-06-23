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

    def move(self, world):
        for i in range(self.__x - 1, self.__x + 2):
            for j in range(self.__y - 1, self.__y + 2):
                if (i != self.__x and j != self.__y) and world.checkPos(i, j):
                    self.setPos(i, j)
                    break

    def show(self, surf):
        pygame.draw.rect(surf, "green", (self.__x * 50, self.__y * 50, 50, 50))
