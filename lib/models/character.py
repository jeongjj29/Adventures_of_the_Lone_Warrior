class Character:
    def __init__(self, name, attack, max_hp, gold, level, exp):
        if not (isinstance(name, str) and len(name) > 0):
            raise Exception("Name must be string longer than 0 characters.")
        if not (
            isinstance(attack, int)
            and isinstance(max_hp, int)
            and isinstance(gold, int)
        ):
            raise Exception("Stats must be an integer.")
        self._name = name
        self._attack = attack
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._gold = gold
        self._level = 1
        self._exp = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (isinstance(name, str) and len(name) > 0):
            raise Exception("Name must be a string longer than 0 charcters.")
        self._name = name

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        if not isinstance(attack, int):
            raise Exception("Attack must be an integer.")
        self._attack = attack

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, max_hp):
        if not isinstance(max_hp, int):
            raise Exception("Max HP must be an integer.")
        self._max_hp = max_hp

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, gold):
        if not isinstance(gold, int):
            raise Exception("Gold must be an integer.")
        self._gold = gold

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if isinstance(level, int) and level > 0:
            self._level = level
        else:
            raise Exception("Level must be an integer greater than 0.")

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, exp):
        if isinstance(exp, int) and exp >= 0:
            self._exp = exp
        else:
            raise Exception("Exp must be an integer greater than or equal to 0.")
