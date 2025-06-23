import pygame

class Player:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def setPos(self, x, y):
        self.__x = x * 50
        self.__y = y * 50
        
    def getPos(self):
        return [self.__x // 50, self.__y // 50]

    def show(self, surf):
        pygame.draw.rect(surf, "white", (self.__x, self.__y, 50,  50))
