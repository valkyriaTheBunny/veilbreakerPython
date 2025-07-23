class Door:
    def __init__(self, dir: str, row: int, col: int):
        self.__dir = dir
        self.__row = row
        self.__col = col

    def getDir(self):
        return self.__dir

    def getRow(self):
        return self.__row

    def getCol(self):
        return self.__col

    def __eq__(self, value):
        if type(value) != Door:
            return False
        return (self.__dir == value.getDir() and self.__col == value.getCol() and self.__row == value.getRow())
