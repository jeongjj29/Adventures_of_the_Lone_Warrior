from models.character import Character
from models.__init__ import CONN, CURSOR


class Equipment:

    all = {}

    def __init__(self, name, attack, max_hp, gold, type, owner_id, id=None):
        self.id = id
        self.name = name
        self.attack = attack
        self.max_hp = max_hp
        self.gold = gold
        self.type = type
        self.owner_id = owner_id

    def __repr__(self):
        return f"{self.name} | Attack: +{self.attack} | Max HP: +{self.max_hp} | Price: {self.gold} | Type: {self.type}"

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if not isinstance(type, str):
            raise Exception("Type must be a string.")
        self._type = type

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        if not (isinstance(owner_id, int) and Character.find_by_id(owner_id)):
            raise Exception("Owner must be a character.")
        self._owner_id = owner_id

    def save(self):
        sql = """
            INSERT INTO equipment (name, attack, max_hp, gold, type, owner_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._gold,
                self._type,
                self._owner_id,
            ),
        )
        CONN.commit()

    def update(self):
        sql = """
            UPDATE equipment
            SET name = ?, attack = ?, max_hp = ?, gold = ?, type = ?, owner_id = ?
            WHERE name = ?
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._gold,
                self._type,
                self._owner_id,
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
                type TEXT,
                owner_id INTEGER,
                FOREIGN KEY(owner_id) REFERENCES characters(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS equipment
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, attack, max_hp, gold, type, owner_id):
        equipment = cls(name, attack, max_hp, gold, type, owner_id)
        equipment.save()
        return equipment

    @classmethod
    def instance_from_db(cls, row):
        equipment = cls.all.get(row[0])
        if equipment:
            equipment.name = row[1]
            equipment.attack = row[2]
            equipment.max_hp = row[3]
            equipment.gold = row[4]
            equipment.type = row[5]
            equipment.owner_id = row[6]
        else:
            equipment = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            equipment.id = row[0]
            cls.all[equipment.id] = equipment
        return equipment

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM equipment
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
