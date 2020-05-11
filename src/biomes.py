# |Boreal taiga_______Swamp_______________Jungle
# |
# |Tundra_____________Forest______________Savanna
# |
# |Arctic_____________Steppe______________Desert>t
from random import choices, randint
from src.db import cursor


class BiomeType:


    def __init__(self):
        self.name = None
        self.temperature_low = 0
        self.humidity_low = 0
        self.temperature_top = 2
        self.humidity_top = 2
        self.size_low = 50
        self.size_top = 100
        # 0 to 10 where 0 is the lowest
        self.low_vegetation_ratio = 0
        self.medium_vegetation_ratio = 0
        self.high_vegetation_ratio = 0
        self.small_prey_ratio = 0
        self.medium_prey_ratio = 0
        self.large_prey_ratio = 0
        # 1 to 99 - how often and how critical changes will be
        # 1 - very stable, 99 - very unstable
        self.stability_low = 1
        self.stability_top = 25

    def calculate_volumes(self):
        self.size = randint(self.size_low, self.size_top)
        return {
            'low_vegetation_volume': int(self.size*self.low_vegetation_ratio*randint(80, 100)/100),
            'medium_vegetation_volume': int(self.size*self.medium_vegetation_ratio*randint(80, 100)/100),
            'high_vegetation_volume': int(self.size*self.high_vegetation_ratio*randint(60, 100)/100),
            'small_prey_volume': int(self.size*self.small_prey_ratio*randint(80, 100)/100),
            'medium_prey_volume': int(self.size*self.medium_prey_ratio*randint(80, 100)/100),
            'large_prey_volume': int(self.size*self.large_prey_ratio*randint(60, 100)/100)
        }

    def randomize_biome(self):
        """Creating randomized biome using current biome type """
        biome = {
            "name": self.name,
            "temperature": randint(self.temperature_low, self.temperature_top),
            "humidity": randint(self.humidity_low, self.humidity_top),
            "size": randint(self.size_low, self.size_top),
            "stability": randint(self.stability_low, self.stability_top),
            "low_vegetation_ratio": self.low_vegetation_ratio,
            "medium_vegetation_ratio": self.medium_vegetation_ratio,
            "high_vegetation_ratio": self.high_vegetation_ratio,
            "small_prey_ratio": self.small_prey_ratio,
            "medium_prey_ratio": self.medium_prey_ratio,
            "large_prey_ratio": self.large_prey_ratio,
        }
        return biome


# BIOMES = (
#     Biome('Arctic', 0, 0, 2, 2),
#     Biome('Tundra', 0, 3, 2, 6),
#     Biome('Taiga', 0, 7, 2, 9),
#     Biome('Steppe', 3, 0, 6, 2),
#     Biome('Forest', 3, 3, 6, 6),
#     Biome('Swamp', 3, 7, 6, 9),
#     Biome('Desert', 7, 0, 9, 2),
#     Biome('Savanna', 7, 3, 9, 6),
#     Biome('Jungle', 7, 7, 9, 9),
# )
class Arctic(BiomeType):

    def __init__(self):
        super().__init__()
        self.name = 'Arctic'
        self.small_prey_ratio = 2
        self.medium_prey_ratio = 3
        self.large_prey_ratio = 10


class Steppe(BiomeType):

    def __init__(self):
        super().__init__()
        self.name = 'Steppe'
        self.temperature_low = 3
        self.humidity_low = 0
        self.temperature_top = 6
        self.humidity_top = 2
        self.low_vegetation_ratio = 10
        self.medium_vegetation_ratio = 5
        self.high_vegetation_ratio = 1
        self.small_prey_ratio = 3
        self.medium_prey_ratio = 3
        self.large_prey_ratio = 5


class Swamp(BiomeType):

    def __init__(self):
        super().__init__()
        self.name = 'Swamp'
        self.temperature_low = 3
        self.humidity_low = 7
        self.temperature_top = 6
        self.humidity_top = 9
        self.low_vegetation_ratio = 8
        self.medium_vegetation_ratio = 4
        self.high_vegetation_ratio = 1
        self.small_prey_ratio = 10
        self.medium_prey_ratio = 3
        self.large_prey_ratio = 1


biomes_pool = (Arctic(), Steppe(), Swamp())
