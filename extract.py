import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

dbConn = sqlite3.connect('assessmentitems.sqlite')
dbConn.row_factory = dict_factory
db = dbConn.cursor()

objects = db.fetchall()

db.execute('SELECT * FROM topic_tools_assessmentitem;')

with open('assesmentData.json', 'w') as outfile:
    json.dump(db.fetchall(), outfile,indent=2)
