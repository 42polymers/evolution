from random import choices
from src.biomes import biomes_pool
from src.db import conn, cursor, db_exists


game_id = 1


def create_db():
    result_biomes = [b.randomize_biome() for b in choices(biomes_pool, k=10)]
    result_biomes = [[b[i] for i in sorted(b.keys())] for b in result_biomes]
    for biome in result_biomes:
        biome.insert(0, game_id)

    cursor.execute("""CREATE TABLE biomes(
    game_id integer,
    high_vegetation_ratio integer , humidity integer ,
    large_prey_ratio integer , low_vegetation_ratio integer ,
    medium_prey_ratio integer , medium_vegetation_ratio integer ,
    name char, biome_size integer , small_prey_ratio integer ,
    stability integer , temperature integer
    )""")

    conn.commit()
    cursor.executemany("INSERT INTO biomes VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", result_biomes)
    conn.commit()


if not db_exists or not cursor.execute('SELECT name FROM sqlite_master').fetchone():
    create_db()
