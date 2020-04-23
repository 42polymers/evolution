from random import randint

from src.db import cursor


game_id = 1


class TurnManager:

    @classmethod
    def get_biomes(cls):
        return cursor.execute(f"""select * from biomes where game_id={game_id}"""
                              ).fetchall()

    @classmethod
    def get_creatures(cls):
        return cursor.execute(
            f"""select * from creatures
            INNER JOIN creature_countable_params
            ON creatures.id = creature_countable_params.creature_id
            INNER JOIN creature_flag_params
            ON creatures.id = creature_flag_params.creature_id
            where creatures.game_id={game_id}"""
                              ).fetchall()

    @classmethod
    def make_turn(cls):
        biomes_data = cls.get_biomes()
        return {
            'biomes_data': cls.calculate_food(biomes_data),
            'creatures_data': cls.calculate_creatures()
        }

    @classmethod
    def calculate_food(cls, biomes_data):
        return [{
            'id': bd['id'],
            'low_vegetation_volume': int(bd['biome_size'] * bd['low_vegetation_ratio'] * randint(80, 100) / 100),
            'medium_vegetation_volume': int(bd['biome_size'] * bd['medium_vegetation_ratio'] * randint(80, 100) / 100),
            'high_vegetation_volume': int(bd['biome_size'] * bd['high_vegetation_ratio'] * randint(60, 100) / 100),
            'small_prey_volume': int(bd['biome_size'] * bd['small_prey_ratio'] * randint(80, 100) / 100),
            'medium_prey_volume': int(bd['biome_size'] * bd['medium_prey_ratio'] * randint(80, 100) / 100),
            'large_prey_volume': int(bd['biome_size'] * bd['large_prey_ratio'] * randint(60, 100) / 100)
        } for bd in biomes_data]

    @classmethod
    def calculate_creatures(cls):
        creatures = cls.get_creatures()
        return [{f: c[f] for f in c if f not in ['game_id']} for c in creatures]
