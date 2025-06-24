import pygame
import random

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
        return self.__x, self.__y

    def move(self, world):
        if not world:
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = self.__x + dx, self.__y + dy
            if world.checkPos(nx, ny):
                print(f"{self.name} moved from ({self.__x}, {self.__y}) to ({nx}, {ny})")
                self.setPos(nx, ny)
                break

    def show(self, surf):
        pygame.draw.rect(surf, "green", (self.__x * 50, self.__y * 50, 50, 50))
