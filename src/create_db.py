from random import choices
from src.biomes import biomes_pool
from src.db import conn, cursor


# cursor.execute("""CREATE TABLE biomes
#                   (
#                     temperature_low INTEGER ,
#                     humidity_low INTEGER ,
#                     temperature_top INTEGER ,
#                     humidity_top INTEGER ,
#                     area INTEGER ,
#                     low_vegetation_ratio INTEGER,
#                     medium_vegetation_ratio INTEGER ,
#                     high_vegetation_ratio INTEGER ,
#                     small_prey_ratio INTEGER ,
#                     medium_prey_ratio INTEGER ,
#                     large_prey_ratio INTEGER
#                    )
#                """)
result_biomes = [b.randomize_biome() for b in choices(biomes_pool, k=10)]
result_biomes = [[b[i] for i in sorted(b.keys())] for b in result_biomes]


cursor.execute("""CREATE TABLE biomes(
high_vegetation_ratio integer , humidity integer ,
large_prey_ratio integer , low_vegetation_ratio integer ,
medium_prey_ratio integer , medium_vegetation_ratio integer ,
name char, biome_size integer , small_prey_ratio integer ,
stability integer , temperature integer
)""")

conn.commit()



cursor.executemany("INSERT INTO biomes VALUES (?,?,?,?,?,?,?,?,?,?,?)", result_biomes)
conn.commit()