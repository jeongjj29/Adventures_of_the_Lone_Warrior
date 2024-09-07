import sqlite3
from character import Character

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
