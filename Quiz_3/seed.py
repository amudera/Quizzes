import csv
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
CSVFILENAME = "TSLA.csv"
DBPATH = os.path.join(DIRNAME, DBFILENAME)
CSVPATH = os.path.join(DIRNAME, CSVFILENAME)

def seed_from_csv(csvpath, dbpath):
    with open(csvpath, 'r') as csvfile, sqlite3.connect(dbpath) as connection:
        reader = csv.DictReader(csvfile)
        curs = connection.cursor()

        curs.execute("""DELETE FROM prices;""")

        for line in reader:
            SQL = """INSERT INTO prices(
                Px_Open,
                Px_High,
                Px_Low,
                Px_Close,
                Adj_Close,
                Volume) VALUES (?, ?, ?, ?, ?, ?);"""

            data = (line['Px_Open'], line['Px_High'],
                    line['Px_Low'],line['Px_Close'],line['Adj_Close'],line['Volume'])

            curs.execute(SQL, data)

            
if __name__ == "__main__":
        seed_from_csv(CSVPATH, DBPATH)