from  world.room import Room
from world.door import Door

class World:
    def __init__(self):
        self.__rooms = []
        self.__doors = []
        self.__level = 1
        self.__roomNum = 0

    def levelUp(self):
        self.__level += 1

    def genRooms(self):
        for i in range(9):
            room = Room()
            self.__rooms.append(room)
            self.__rooms[i].genRoom(self.__level)
            if i <= 7:
                for k in range(23, 0, -1):
                    if self.__rooms[i].checkPos(k, 7):
                        break
                self.__rooms[i].updateGrid(k, 7, "door")
                self.__doors.append(Door("right", i))

            if i > 0:
                for k in range(23):
                    if self.__rooms[i].checkPos(k, 7):
                        break
                self.__rooms[i].updateGrid(k, 7, "door")
                self.__doors.append(Door("left", i))

    def __moveRoom(self, dir: str):
        if dir == "right" and self.__roomNum < 8:
            self.__roomNum += 1
        elif dir == "left" and self.__roomNum > 0:
            self.__roomNum -= 1

    def show(self, surf):
        self.__rooms[self.__roomNum].show(surf)

    def sPos(self):
        #generates a starting position for the player (the first non wall)
        for i in range(self.__rooms[self.__roomNum].width):
            for j in range(self.__rooms[self.__roomNum].height):
                if self.__rooms[self.__roomNum].checkPos(i, j):
                    return [i, j]

    def update(self, player, dt):
        self.__rooms[self.__roomNum].update(player, dt)

    def updateGrid(self, x: int, y: int, value: str):
        self.__rooms[self.__roomNum].updateGrid(x, y, value)

    def isDoor(self, x: int, y: int, dir: str):
        tDoor = Door(dir, self.__roomNum)

        try:
            index = self.__doors.index(tDoor)

            if index >= 0:
                self.__moveRoom(dir)
                self.updateGrid(x - 1, y, "floor")
        except ValueError:
            pass

    def checkPos(self, x: int, y: int, value: str = "floor"):
        return  self.__rooms[self.__roomNum].checkPos(x, y, value)

    def isOccupied(self, x: int, y: int, atkVal: int):
        return self.__rooms[self.__roomNum].isOccupied(x, y, atkVal)

    def runFount(self, player):
        self.__rooms[self.__roomNum].runFount(player)

    def empty(self):
        for room in self.__rooms:
            if not room.isEmpty():
                return False

        return True
