import os
import sqlite3


db_path = os.path.join(os.path.dirname(os.getcwd()), 'evo.db')
db_exists = os.path.isfile(db_path)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect(db_path)
conn.row_factory = dict_factory
cursor = conn.cursor()
