class Equipment:
    def __init__(self, name: str, defense: int = 0, attack: int = 0):
        self._name = name
        self._atk = attack
        self._def = defense
