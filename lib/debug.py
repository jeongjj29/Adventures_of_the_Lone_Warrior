#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
from models.enemy import Enemy

from models.__init__ import CONN, CURSOR
import ipdb


def reset_database():
    Character.drop_table()
    Enemy.drop_table()
    Character.create_table()
    Enemy.create_table()

    Character.create("Player", 10, 100, 0)
    Enemy.create("Slime", 5, 20, 10)
    Enemy.create("Spider", 10, 40, 20)
    Enemy.create("Zombie", 15, 60, 30)
    Enemy.create("Dragon", 20, 80, 40)


reset_database()
ipdb.set_trace()
