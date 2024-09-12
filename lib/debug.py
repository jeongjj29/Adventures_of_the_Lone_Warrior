#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
from models.enemy import Enemy
from models.equipment import Equipment

from models.__init__ import CONN, CURSOR
import ipdb


def reset_database():
    Character.drop_table()
    Enemy.drop_table()
    Equipment.drop_table()
    Character.create_table()
    Enemy.create_table()
    Equipment.create_table()

    merchant = Character.create("Merchant", 1000, 1000, 1000, 10000, 100, 0)

    Enemy.create("Slime", 5, 20, 10, "cave")
    Enemy.create("Spider", 10, 40, 20, "forest")
    Enemy.create("Zombie", 15, 60, 30, "graveyard")
    Enemy.create("Dragon", 20, 80, 40, "den")

    Equipment.create("Wooden Sword", 5, 0, 10, "weapon", merchant.id)
    Equipment.create("Iron Sword", 10, 0, 20, "weapon", merchant.id)
    Equipment.create("Diamond Sword", 20, 0, 50, "weapon", merchant.id)
    Equipment.create("Mithril Sword", 30, 0, 100, "weapon", merchant.id)
    Equipment.create("Adamantium Sword", 40, 0, 200, "weapon", merchant.id)
    Equipment.create("Wooden Armor", 0, 5, 10, "armor", merchant.id)
    Equipment.create("Iron Armor", 0, 10, 20, "armor", merchant.id)
    Equipment.create("Diamond Armor", 0, 20, 50, "armor", merchant.id)
    Equipment.create("Mithril Armor", 0, 30, 100, "armor", merchant.id)
    Equipment.create("Adamantium Armor", 0, 40, 200, "armor", merchant.id)


reset_database()
ipdb.set_trace()
