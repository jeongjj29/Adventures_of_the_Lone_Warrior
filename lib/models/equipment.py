from models.character import Character


class Equipment:
    def __init__(self, name, attack, max_hp, gold, owner):
        self._name = name
        self._attack = attack
        self._max_hp = max_hp
        self._gold = gold
        self._owner = owner

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
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
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Character):
            raise Exception("Owner must be a character.")
        self._owner = owner

    def change_owner(self, buyer, seller):
        if buyer.gold - self.gold < 0:
            print("Not enough gold.")
        buyer.gold -= self.gold
        seller.gold += self.gold
        self.owner = buyer
