from models.__init__ import CONN, CURSOR


class Enemy:

    all = {}

    def __init__(self, name, attack, max_hp, gold):
        if not (isinstance(name, str) and len(name) > 0):
            raise Exception("Name must be string longer than 0 enemies.")
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

    def __repr__(self):
        return f"{self.name} | HP: {self.current_hp} / {self.max_hp} | Attack: {self.attack}"

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
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, current_hp):
        if not isinstance(current_hp, int):
            raise Exception("Current HP must be an integer.")
        self._current_hp = current_hp

    def defend(self, damage):
        self._current_hp -= damage

    def save(self):
        sql = """
            INSERT INTO enemies (name, attack, max_hp, current_hp, gold)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (
                self._name,
                self._attack,
                self._max_hp,
                self._current_hp,
                self._gold,
            ),
        )
        CONN.commit()

    def update(self):
        sql = """
            UPDATE enemies
            SET name = ?, attack = ?, max_hp = ?, current_hp = ?, gold = ?
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
                self._id,
            ),
        )
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM enemies
            WHERE id = ?
        """
        CURSOR.execute(sql, (self._id,))
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS enemies (
                id INTEGER PRIMARY KEY,
                name TEXT,
                attack INTEGER,
                max_hp INTEGER,
                current_hp INTEGER,
                gold INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS enemies
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, attack, max_hp, gold):
        enemy = cls(name, attack, max_hp, gold)
        enemy.save()
        return enemy

    @classmethod
    def instance_from_db(cls, row):
        enemy = cls.all.get(row[0])
        if enemy:
            enemy.name = row[1]
            enemy.attack = row[2]
            enemy.max_hp = row[3]
            enemy.current_hp = row[4]
            enemy.gold = row[5]
        else:
            enemy = cls(row[1], row[2], row[3], row[4], row[5])
            enemy.id = row[0]
        return enemy

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * 
            FROM enemies
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
