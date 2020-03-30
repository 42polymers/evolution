from random import randint

from src.db import cursor


game_id = 1


class TurnManager:

    @classmethod
    def get_biomes(cls):
        biomes = cursor.execute(f"""select * from biomes where game_id={game_id}"""
                                ).fetchall()
        return biomes

    @classmethod
    def make_turn(cls):
        biomes_data = cls.get_biomes()
        return cls.calculate_food(biomes_data)

    @classmethod
    def calculate_food(cls, biomes_data):
        return [{
            'low_vegetation_volume': int(bd['biome_size'] * bd['low_vegetation_ratio'] * randint(80, 100) / 100),
            'medium_vegetation_volume': int(bd['biome_size'] * bd['medium_vegetation_ratio'] * randint(80, 100) / 100),
            'high_vegetation_volume': int(bd['biome_size'] * bd['high_vegetation_ratio'] * randint(60, 100) / 100),
            'small_prey_volume': int(bd['biome_size'] * bd['small_prey_ratio'] * randint(80, 100) / 100),
            'medium_prey_volume': int(bd['biome_size'] * bd['medium_prey_ratio'] * randint(80, 100) / 100),
            'large_prey_volume': int(bd['biome_size'] * bd['large_prey_ratio'] * randint(60, 100) / 100)
        } for bd in biomes_data]