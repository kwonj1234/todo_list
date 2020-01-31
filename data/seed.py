import sqlite3
import os

DIR = os.path.dirname(__file__) #works regardless of the os you're using
DBPATH = os.path.join(DIR, 'todo.db')

def seed(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = """INSERT INTO todoitems (
            pk , title, description, complete
            ) VALUES (
            1, "test.db", "test our db", 0
            );"""
        cur.execute(SQL)

if __name__ == "__main__":
    seed()
