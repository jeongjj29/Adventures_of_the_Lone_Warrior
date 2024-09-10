from models.character import Character
from models.__init__ import CONN, CURSOR


class Equipment:
    def __init__(self, name, attack, max_hp, gold, owner):
        self.name = name
        self.attack = attack
        self.max_hp = max_hp
        self.gold = gold
        self.owner_id = owner

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
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        if not (isinstance(owner_id, int) and Character.find_by_id(owner_id)):
            raise Exception("Owner must be a character.")
        self._owner = owner_id

    def change_owner(self, buyer_id):
        if buyer_id.gold - self.gold < 0:
            print("Not enough gold.")
        buyer_id.gold -= self.gold
        seller_id.gold += self.gold
        self.owner = buyer_id

    def save(self):
        sql = """
            INSERT INTO equipment (name, attack, max_hp, gold, owner_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._gold,
                self._owner_id,
            ),
        )
        CONN.commit()

    def update(self):
        sql = """
            UPDATE equipment
            SET name = ?, attack = ?, max_hp = ?, gold = ?, owner_id = ?
            WHERE name = ?
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._gold,
                self._owner,
                self._name,
            ),
        )
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM equipment
            WHERE name = ?
        """
        CURSOR.execute(sql, (self._id,))
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS equipment (
                id INTEGER PRIMARY KEY,
                name TEXT,
                attack INTEGER,
                max_hp INTEGER,
                gold INTEGER,
                owner_id INTEGER,
                FOREIGN KEY(owner_id) REFERENCES characters(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
