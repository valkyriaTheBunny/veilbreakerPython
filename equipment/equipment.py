class Equipment:
    def __init__(self, name: str, defense: int = 0, attack: int = 0):
        self.__name = name
        self.__atk = attack
        self.__def = defense
