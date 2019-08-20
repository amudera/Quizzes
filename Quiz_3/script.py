import csv
from orm import ORM
from tsla_data import TSLA
TSLA.bpath = 't'

fields = ['Px_Open','Px_High','Px_Low','Px_Close','Adj_Close','Volume']

with open ('TSLA.csv') as csv_file:
    reader = csv.Dictreader(csv_file,fieldnames=fields)
    for row in reader:
        tlsa_entry = TSLA(**row)
        tsla_entry.save()