from  world.room import Room
from world.door import Door

class World:
    def __init__(self):
        self.__rooms = []
        self.__doors = []
        self.__level = 1
        self.__row = 0
        self.__roomNum = 0

    def levelUp(self):
        self.__level += 1

    def genRooms(self):
        for i in range(3):
            self.__rooms.append([])
            for j in range(3):
                room = Room()
                self.__rooms[i].append(room)
                self.__rooms[i][j].genRoom(self.__level)
                if i < 3:
                    for k in range(23, 0, -1):
                        if self.__rooms[i][j].checkPos(k, 7):
                            break
                    self.__rooms[i][j].updateGrid(k, 7, "door")
                    self.__doors.append(Door("right", i, j))
                if j < 3:
                    for k in range(13, 0, -1):
                        if self.__rooms[i][j].checkPos(12, k):
                            break
                    self.__rooms[i][j].updateGrid(12, k, "door")
                    self.__doors.append(Door("down", i, j))

    def __moveRoom(self, dir: str):
        if dir == "left" and self.__roomNum > 0:
            self.__rooomNum -= 1
        elif dir == "right" and self.__roomNum < 3:
            self.__roomNum += 1
        elif dir == "up" and self.__row > 0:
            self.__row -= 1
        elif dir == "down" and self.__row < 3:
            self.__row += 1

    def show(self, surf):
        self.__rooms[self.__row][self.__roomNum].show(surf)

    def sPos(self):
        #generates a starting position for the player (the first non wall)
        for i in range(self.__rooms[0][0].width):
            for j in range(self.__rooms[0][0].height):
                if self.__rooms[self.__row][self.__roomNum].checkPos(i, j):
                    return [i, j]

    def update(self, player, dt):
        self.__rooms[self.__row][self.__roomNum].update(player, dt)

    def updateGrid(self, x: int, y: int, value: str):
        self.__rooms[self.__row][self.__roomNum].updateGrid(x, y, value)

    def isDoor(self, x: int, y: int, dir: str):
        tDoor = Door(dir, self.__row, self.__roomNum)

        try:
            index = self.__doors.index(tDoor)
            self.__moveRoom(dir)
        except ValueError:
            print("Error")

    def checkPos(self, x: int, y: int, value: str = "floor"):
        return  self.__rooms[self.__row][self.__roomNum].checkPos(x, y, value)

    def isOccupied(self, x: int, y: int, atkVal: int):
        return self.__rooms[self.__row][self.__roomNum].isOccupied(x, y, atkVal)
