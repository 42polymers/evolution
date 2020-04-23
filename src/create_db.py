from random import choices
from src.biomes import biomes_pool
from src.creatures import Creature
from src.db import conn, cursor, db_exists


game_id = 1


def create_biomes():
    result_biomes = [b.randomize_biome() for b in choices(biomes_pool, k=10)]
    result_biomes = [[b[i] for i in sorted(b.keys())] for b in result_biomes]
    for biome in result_biomes:
        biome.insert(0, game_id)

    cursor.execute("""CREATE TABLE biomes(
    id integer primary key autoincrement not null,
    game_id integer,
    high_vegetation_ratio integer , humidity integer ,
    large_prey_ratio integer , low_vegetation_ratio integer ,
    medium_prey_ratio integer , medium_vegetation_ratio integer ,
    name char, biome_size integer , small_prey_ratio integer ,
    stability integer , temperature integer
    )""")

    conn.commit()
    cursor.executemany("INSERT INTO biomes VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?)", result_biomes)
    conn.commit()


def create_creatures():

    creatures = [Creature(f'creature_{b}', 50).randomize_creature() for b in range(10)]

    main = [c['main'] for c in creatures]
    count = [c['count'] for c in creatures]
    flag = [c['flag'] for c in creatures]

    main = [[b[i] for i in sorted(b.keys())] for b in main]
    count = [[b[i] for i in sorted(b.keys())] for b in count]
    flag = [[b[i] for i in sorted(b.keys())] for b in flag]

    cursor.execute("""CREATE TABLE creatures(
    id integer primary key autoincrement not null,
    game_id integer NOT NULL,
    name CHAR NOT NULL
    )""")

    cursor.execute("""CREATE TABLE creature_countable_params(
    creature_id integer primary key autoincrement not null,
    game_id integer NOT NULL,
    frame integer NOT NULL CHECK (frame BETWEEN 0 AND 10),
    musculature integer NOT NULL CHECK (musculature BETWEEN 0 AND 10),
    FOREIGN KEY (creature_id) REFERENCES creatures(id) ON DELETE CASCADE 
    )""")

    cursor.execute("""CREATE TABLE creature_flag_params(
    creature_id integer primary key autoincrement not null,
    game_id integer NOT NULL,
    warmblooded integer NOT NULL DEFAULT  0 CHECK (warmblooded IN (0, 1)),
    FOREIGN KEY (creature_id) REFERENCES creatures(id) ON DELETE CASCADE
    )""")

    conn.commit()
    cursor.executemany(f"INSERT INTO creatures VALUES (null,{game_id},?)", main)
    conn.commit()

    fks = range(cursor.lastrowid - len(main), cursor.lastrowid)

    for arr in (count, flag):
        for j, i in enumerate(arr):
            i.insert(0, game_id)
            i.insert(0, fks[j])

    cursor.executemany("INSERT INTO creature_countable_params"
                       " VALUES (?,?,?,?)", count)
    cursor.executemany("INSERT INTO creature_flag_params"
                       " VALUES (?,?,?)", flag)
    conn.commit()


def create_db():
    create_biomes()
    create_creatures()


if not db_exists or not cursor.execute('SELECT name FROM sqlite_master').fetchone():
    create_db()
