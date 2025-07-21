import pygame
import random

class Generic:
    def __init__(self, name: str, health: int, equip, color: str):
        self.name = name
        self.health = health
        self.equip = equip
        self.color = color
        self.__x = 0
        self.__y = 0


    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getPos(self):
        return self.__x, self.__y

    def move(self, world, player):
        if not world:
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = self.__x + dx, self.__y + dy
            if world.checkPos(nx, ny):
                world.getGrid()[self.__x][self.__y] = "floor"
                self.setPos(nx, ny)
                break
            if world.checkPos(nx, ny, "player"):
                self.__attack(player)

    def __attack(self, target):
        target.health -= self.equip.damage()

    def show(self, surf):
        pygame.draw.rect(surf, self.color, (self.__x * 50, self.__y * 50, 50, 50))
