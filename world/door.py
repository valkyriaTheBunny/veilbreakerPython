class Door:
    def __init__(self, dir: str, row: int):
        self.__dir = dir
        self.__row = row

    def getDir(self):
        return self.__dir

    def getRow(self):
        return self.__row

    def __eq__(self, value):
        if type(value) != Door:
            return False
        return (self.__dir == value.getDir() and self.__row == value.getRow())
