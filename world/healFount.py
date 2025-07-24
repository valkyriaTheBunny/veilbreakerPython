class Fountain:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def heal(self, player):
        player.modHealth()
