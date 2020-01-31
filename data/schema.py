import sqlite3
import os

DIR = os.path.dirname(__file__) #works regardless of the os you're using
DBPATH = os.path.join(DIR, 'todo.db')

def schema(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = """CREATE TABLE todoitems (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128),
            description TEXT, 
            complete INTEGER
        );"""
        #TEXT just allows for a bunch of text better than VARCHAR but you still don't want it to be too long, not like a book
        cur.execute(SQL)

if __name__ == "__main__":
    schema()

