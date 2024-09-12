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

    # Name, Attack, Max HP, Gold, Location
    Enemy.create("Slime", 5, 200, 10, "cave")
    Enemy.create("Slime", 5, 200, 10, "cave")
    Enemy.create("Giant Slime", 10, 400, 20, "cave")
    Enemy.create("Giant Slime", 10, 400, 20, "cave")
    Enemy.create("Rimuru", 50, 10000, 1000, "cave")

    Enemy.create("Spider", 10, 400, 20, "forest")
    Enemy.create("Goblin", 10, 400, 60, "forest")
    Enemy.create("Orc", 20, 800, 100, "forest")
    Enemy.create("Troll", 30, 1000, 150, "forest")
    Enemy.create("Hamsuke", 50, 10000, 1000, "forest")

    Enemy.create("Zombie", 15, 600, 30, "graveyard")
    Enemy.create("Skeleton", 20, 800, 50, "graveyard")
    Enemy.create("Vampire", 30, 1000, 80, "graveyard")
    Enemy.create("Death Knight", 50, 3000, 200, "graveyard")
    Enemy.create("Lich", 55, 7000, 900, "graveyard")

    Enemy.create("Wyvern", 20, 800, 40, "den")
    Enemy.create("Griffon", 30, 1200, 80, "den")
    Enemy.create("Dragon", 50, 3000, 250, "den")
    Enemy.create("Hydra", 75, 10000, 1000, "den")
    Enemy.create("Veldora", 100, 25000, 4000, "den")

    # Name, Attack, Max HP, Gold, Type, Owner ID
    Equipment.create("Wooden Sword", 5, 0, 10, "weapon", merchant.id)
    Equipment.create("Iron Sword", 10, 0, 50, "weapon", merchant.id)
    Equipment.create("Diamond Sword", 20, 0, 100, "weapon", merchant.id)
    Equipment.create("Mithril Sword", 30, 0, 300, "weapon", merchant.id)
    Equipment.create("Adamantium Sword", 40, 0, 500, "weapon", merchant.id)
    Equipment.create("Wooden Armor", 0, 10, 10, "armor", merchant.id)
    Equipment.create("Iron Armor", 0, 50, 50, "armor", merchant.id)
    Equipment.create("Diamond Armor", 0, 100, 100, "armor", merchant.id)
    Equipment.create("Mithril Armor", 0, 300, 300, "armor", merchant.id)
    Equipment.create("Adamantium Armor", 0, 500, 500, "armor", merchant.id)
    Equipment.create("Excalibur", 100, 1000, 1000, "weapon", merchant.id)


reset_database()
ipdb.set_trace()
