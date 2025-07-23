from characters.monGenerator import Generator
from random import randint
from datetime import datetime
from collections import deque
import pygame, random, pickle

class World:
    def __init__(self):
        self.__height = 14
        self.__width = 24
        self.__monList = []
        self.__grid = []
        self.__generator = Generator()
        ms = datetime.time(datetime.now()).microsecond
        random.seed(ms * 500000 + ms ** 2)

    def __genNoise(self):
        #generates a starting map of wall and floor tiles
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
        #smoothing to make the map more traversable
        #sets the new values to a different grid
        #then assigns the new grid to the original
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
        #makes sure the floor area is all reachable
        #so the player and enemies are not ever trapped
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
            #runs map generation methods until a completely
            #traversable map is found
            self.__genNoise()
            self.__smoothing()
            sx, sy = self.sPos()
            if self.__is_area_connected(sx, sy):
                break

        #randomly generates monster starting positions
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "floor" and randint(40, 1000) < 55:
                    #generates a random monster class instance
                    #marking its initially position as occupied so that
                    #multiple monsters cannot spawn on the same square

                    mon = self.__generator.create(level)
                    mon.setPos(i, j)
                    self.__grid[i][j] = "occupied"
                    self.__monList.append(mon)

    def show(self, surf: pygame.surface):
        #shows the map
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__grid[i][j] == "wall":
                    pygame.draw.rect(surf, "purple", (i * 50, j * 50, 50, 50))
                else:
                    pygame.draw.rect(surf, "gold", (i * 50, j * 50, 50, 50))

        for mon in self.__monList:
            mon.show(surf)

    def update(self, player, dt):
        #updates the world, specifically monsters in the world
        #needs dt so that monsters can move independent of the player
        #and player so that monsters can attack the player
        for i, mon in enumerate(self.__monList):
            if mon.health <= 0:
                self.__monList.pop(i)
            else:
                mon.move(self, player, dt)

    def sPos(self):
        #generates a starting position for the player (the first non wall)
        for i in range(self.__width):
            for j in range(self.__height):
                if self.checkPos(i, j):
                    return [i, j]

    def checkPos(self, x: int, y: int, value:str = "floor"):
        #checks if a grid coordinate's value is equal to a given value
        #generally used for movement with a default of 'floor'
        #but also used to check for whether combat should happen
        #with the values 'occupied' and 'player'
        if x < 0 or y < 0 or x >= self.__width or y >= self.__height:
            return False
        return self.__grid[x][y] == value

    def getGrid(self, x = None, y = None, atkVal = None):
        #returns a monster if there is a monster at a given grid location
        #or false if there is no monster
        #or if no position is given, returns the grid
        #the return grid functionality is useful for
        #updating grid locations to and from occupied
        if x and y:
            for i, mon in enumerate(self.__monList):
                if mon.getPos() == (x, y) and mon.health <= atkVal:
                   self.__monList.pop(i)
                   self.__grid[x][y] = "floor"
                elif mon.getPos() == (x, y):
                    return mon
            return False
        else:
            return self.__grid
