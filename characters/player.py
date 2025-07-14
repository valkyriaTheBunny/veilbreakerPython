import pygame

class Player:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__equipment = "Dagger"

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getPos(self):
        return [self.__x, self.__y]

    def show(self, surf):
        pygame.draw.rect(surf, "white", (self.__x * 50, self.__y * 50, 50,  50))
