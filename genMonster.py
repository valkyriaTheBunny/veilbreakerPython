from math import sqrt
from random import choice
import pygame

class Generic:
    def __init__(self, name, health, equip):
        self.__moves = [[0,1], [0, -1], [1, 0], [-1, 0]]
        self.name = name
        self.health = health
        self.equip = equip
        self.__x = 0
        self.__y = 0


    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, target, world):
        moves = self.__moves
        pos = target.getPos()
        dist = sqrt(((self.__x - pos[0]) ** 2) + ((self.__y - pos[1]) ** 2))
        chosen = None

        for move in self.__moves:
            newMonPosX = self.__x + move[0]
            newMonPosY = self.__y + move[1]
            if world.checkPos(newMonPosX, newMonPosY):
                dist2 = sqrt(((newMonPosX - pos[0]) ** 2) + ((newMonPosY - pos[1]) ** 2))
                if dist2 < dist:
                    chosen = move
                    break

        while chosen == None:
            if moves[0]:
                chosen = choice(moves)
                newMonPosX = self.__x + chosen[0]
                newMonPosY = self.__y + chosen[1]
                if not world.checkPos(newMonPosX, newMonPosY):
                    moves.remove(chosen)
                    chosen = None

        self.__x = self.__x + chosen[0]
        self.__y = self.__y + chosen[1]

    def show(self, surf):
        pygame.draw.rect(surf, "green", (self.__x * 50, self.__y * 50, 50, 50))
