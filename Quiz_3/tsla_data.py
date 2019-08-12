import sqlite3
import os
from orm import ORM

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
DBPATH = os.path.join(DIRNAME, DBFILENAME)

class TSLA:
    tablename = "prices"
    fields = ['Px_Open','Px_High','Px_Low','Px_Close','Adj_Close','Volume']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.open = kwargs.get("Px_Open")
        self.high = kwargs.get("Px_High")
        self.low = kwargs.get("Px_Low")
        self.close = kwargs.get("Px_Close")
        self.adjclose = kwargs.get("Adj_Close")
        self.volume = kwargs.get("Volume")
    
    def get_px_open(self):
