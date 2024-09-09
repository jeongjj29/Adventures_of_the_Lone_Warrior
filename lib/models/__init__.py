import sqlite3

CONN = sqlite3.connect("adventure.db")
CURSOR = CONN.cursor()
