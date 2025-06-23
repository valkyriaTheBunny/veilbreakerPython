from world import World
from math import sqrt
import pygame

class Generic:
    def __init__(self, name, health, equip):
        self.__moves = [[0,1], [0, -1], [1, 0], [-1, 0]]
        self.__name = name
        self.__health = health
        self.__equip = equip
        self.__x = 0
        self.__y = 0

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, target):
        pos = target.getPos()
        dist = sqrt(((self.__x - pos[0]) ** 2) + ((self.__y - pos[1]) ** 2))
        chosen = None

        for move in self.__moves:
            newMonPosX = self.__x + move[0]
            newMonPosY = self.__y + move[1]
            if World.checkPos(newMonPosX, newMonPosY):
                dist2 = sqrt(((newMonPosX - pos[0]) ** 2) + ((newMonPosY - pos[1]) ** 2))
                if dist2 < dist:
                    chosen = move
                    break

        self.__x = self.__x + chosen[0]
        self.__y = self.__y + chosen[1]

    def show(self, surf):
        pygame.draw.rect(surf, "green", self.__x * 50, self.__y * 50, 50, 50)
