from equipment.equipment import Equipment

class Weapon(Equipment):
    def __init__(self, name, attack):
        super().__init__(name, attack = attack)

    def damage(self):
        print(self.__atk)
        return self.__atk
