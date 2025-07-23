import pygame
import random

class Generic:
    def __init__(self, name: str, health: int, equip, color: str, time: int):
        self.name = name
        self.health = health
        self.equip = equip
        self.color = color
        self.__start = 0
        self.__time = time
        self.__x = 0
        self.__y = 0

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getPos(self):
        return self.__x, self.__y

    def move(self, world, player, dt):
        if not world:
            return

        if dt - self.__start > self.__time:
            self.__start = dt
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = self.__x + dx, self.__y + dy
                if world.checkPos(nx, ny, "player"):
                    self.attack(player)
                    player.attack(self)
                if world.checkPos(nx, ny):
                    world.updateGrid(self.__x, self.__y, "floor")
                    self.setPos(nx, ny)
                    world.updateGrid(self.__x, self.__y, "occupied")
                    break

    def attack(self, target):
        target.health -= self.equip.damage()

    def show(self, surf):
        pygame.draw.rect(surf, self.color, (self.__x * 50, self.__y * 50, 50, 50))
        pygame.draw.rect(surf, (255, 0, 0), (self.__x * 50, self.__y * 50 + 45, self.health, 5))
