from character import Character
from enemy import Enemy


class Battle:
    def __init__(self, player, enemy):
        if not (isinstance(player, Character) and isinstance(enemy, Enemy)):
            raise Exception
        self._player = player
        self._enemy = enemy

    @property
    def player(self):
        return self._player

    @property
    def enemy(self):
        return self._enemy
