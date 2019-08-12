import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'tsla.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS prices;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE prices (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Px_Open FLOAT,
            Px_High FLOAT,
            Px_Low FLOAT,
            Px_Close FLOAT,
            Adj_Close FLOAT,
            Volume INTEGER
        ); """
        cur.execute(SQL)


if __name__ == "__main__":
    schema()