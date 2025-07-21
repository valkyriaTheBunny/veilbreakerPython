from equipment.weapons import Weapon
import pygame

class Player:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__equip = Weapon("Dagger", 5)
        self.level = 0
        self.health = 100
        self.experience = 0

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getAtkVal(self):
        return self.__equip.damage()

    def attack(self, target):
        target.health -= self.__equip.damage()

    def getPos(self):
        return [self.__x, self.__y]

    def show(self, surf):
        pygame.draw.rect(surf, "white", (self.__x * 50, self.__y * 50, 50,  50))
