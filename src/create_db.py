import os
import sqlite3
from random import randint


conn = sqlite3.connect(os.path.join(os.path.dirname(os.getcwd()), 'evo.db'))
cursor = conn.cursor()
cursor.execute("""CREATE TABLE biomes
                  (
                    temperature_low INTEGER ,
                    humidity_low INTEGER ,
                    temperature_top INTEGER ,
                    humidity_top INTEGER ,
                    area INTEGER ,
                    low_vegetation_ratio INTEGER,
                    medium_vegetation_ratio INTEGER ,
                    high_vegetation_ratio INTEGER ,
                    small_prey_ratio INTEGER ,
                    medium_prey_ratio INTEGER ,
                    large_prey_ratio INTEGER 
                   )
               """)

conn.commit()

biomes = [[randint(0, 10) for j in range(11)] for i in range(5)]

cursor.executemany("INSERT INTO biomes VALUES (?,?,?,?,?,?,?,?,?,?,?)", biomes)
conn.commit()