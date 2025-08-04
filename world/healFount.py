class Fountain:
    def __init__(self, x, y, uses):
        self.__x = x
        self.__y = y
        self.__uses = uses

    def heal(self, player):
        if self.__uses > 0:
            player.modHealth()
            self.__uses -= 1
