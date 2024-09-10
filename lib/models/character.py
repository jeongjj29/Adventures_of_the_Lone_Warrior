from models.__init__ import CONN, CURSOR


class Character:

    all = {}

    def __init__(self, name, attack, max_hp, current_hp, gold, level, exp, id=None):
        self.id = id
        self.name = name
        self.attack = attack
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.gold = gold
        self.level = level
        self.exp = exp

    def __repr__(self):
        return f"{self.name} | HP: {self.current_hp} / {self.max_hp} | Attack: {self.attack} | Gold: {self.gold} | Level: {self.level} | Exp: {self.exp} / {100 * (self.level ** 2)}"

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

    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, current_hp):
        if isinstance(current_hp, int):
            if current_hp > self.max_hp:
                self._current_hp = self.max_hp
            else:
                self._current_hp = current_hp
        else:
            raise Exception("Current HP must be an integer.")

    def defend(self, damage):
        self.current_hp -= damage

    def level_up(self, exp_gain):
        self.exp += exp_gain
        if self.exp >= 100 * self._level**2:
            self._level += 1
            self._attack += 5
            self._max_hp += 100
            self._current_hp = self._max_hp
            print(f"You have gained {exp_gain} exp.")
            print(f"You have leveled up to level {self._level}!")
        else:
            print(f"You have gained {exp_gain} exp.")

    def inventory(self):
        sql = """
            SELECT *
            FROM equipment
            WHERE owner_id = ?
        """
        return CURSOR.execute(sql, (self.id,)).fetchall()

    def save(self):
        sql = """
            INSERT INTO characters (name, attack, max_hp, current_hp, gold, level, exp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._current_hp,
                self._gold,
                self._level,
                self._exp,
            ),
        )
        CONN.commit()

    def update(self):
        sql = """
            UPDATE characters
            SET name = ?, attack = ?, max_hp = ?, current_hp = ?, gold = ?, level = ?, exp = ?
            WHERE id = ?
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._current_hp,
                self._gold,
                self._level,
                self._exp,
                self._id,
            ),
        )
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM characters
            WHERE id = ?
        """
        CURSOR.execute(sql, (self._id,))
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY,
                name TEXT,
                attack INTEGER,
                max_hp INTEGER,
                current_hp INTEGER,
                gold INTEGER,
                level INTEGER,
                exp INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS characters
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, attack, max_hp, current_hp, gold, level, exp):
        character = cls(name, attack, max_hp, current_hp, gold, level, exp)
        character.save()
        return character

    @classmethod
    def instance_from_db(cls, row):
        character = cls.all.get(row[0])
        if character:
            character.name = row[1]
            character.attack = row[2]
            character.max_hp = row[3]
            character.current_hp = row[4]
            character.gold = row[5]
            character.level = row[6]
            character.exp = row[7]
        else:
            character = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            character.id = row[0]
            cls.all[character.id] = character
        return character

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM characters
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
