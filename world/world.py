from random import randint
from datetime import datetime
from collections import deque
import pygame, random
from characters.monGenerator import Generator

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.__monList = []
        self.__grid = []
        self.__generator = Generator()
        ms = datetime.time(datetime.now()).microsecond
        random.seed(ms * 100000 + ms)

    def __genNoise(self):
        noiseDen = 65
        for i in range(self.__width):
            self.__grid.append([])
            for _ in range(self.__height):
                gen = randint(-1, 101)
                if gen >= noiseDen:
                    self.__grid[i].append("wall")
                else:
                    self.__grid[i].append("floor")

    def __smoothing(self, iterations:int =10):
        width, height = self.__width, self.__height
        for _ in range(iterations):
            new_grid = [["wall"] * height for _ in range(width)]
            for x in range(width):
                for y in range(height):
                    walls = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < width and 0 <= ny < height:
                                if self.__grid[nx][ny] == "wall":
                                    walls += 1
                            else:
                                walls += 1
                    new_grid[x][y] = "floor" if walls < 5 else "wall"
            self.__grid = new_grid

    def __is_area_connected(self, start_x: int, start_y: int):
        visited = set()
        queue = deque([(start_x, start_y)])
        visited.add((start_x, start_y))

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.__width and 0 <= ny < self.__height:
                    if (nx, ny) not in visited and self.__grid[nx][ny] == "floor":
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        total_floor = sum(row.count("floor") for row in self.__grid)
        return len(visited) == total_floor

    def genRoom(self, level: int):
        while True:
            self.__genNoise()
            self.__smoothing(10)
            sx, sy = self.sPos()
            if self.__is_area_connected(sx, sy):
                break

        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "floor" and randint(0, 300) < 55:
                    if self.__grid[i][j] != "occupied":
                        mon = self.__generator.create(level)
                        mon.setPos(i, j)
                        self.__grid[i, j] = "occupied"
                        self.__monList.append(mon)

    def show(self, surf: pygame.surface):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "wall":
                    pygame.draw.rect(surf, "purple", (i * 50, j * 50, 50, 50))
                else:
                    pygame.draw.rect(surf, "gold", (i * 50, j * 50, 50, 50))

        for mon in self.__monList:
            mon.show(surf)

    def update(self):
        for mon in self.__monList:
            mon.move(self)

    def sPos(self):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.checkPos(i, j):
                    return [i, j]

    def makeUnoccupied(self, x, y):
        self.__grid[x][y] = "floor"

    def checkPos(self, x: int, y: int, value:str = "floor"):
        if x < 0 or y < 0 or x >= self.__width or y >= self.__height:
            return False
        return self.__grid[x][y] == value

    def loadBattleScene():
        pass
