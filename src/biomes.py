# BIOMES = {}
# |Boreal taiga_______Swanp_______________Jungle
# |
# |Tundra_____________Forest______________Savanna
# |
# |Arctic_____________Steppe______________Desert>t
from random import randint


class Biome:

    def __init__(self, size):
        self.temperature_low = 0
        self.humidity_low = 0
        self.temperature_top = 2
        self.humidity_top = 2
        self.size = size
        self.low_vegetation_ratio = 0
        self.medium_vegetation_ratio = 0
        self.high_vegetation_ratio = 0
        self.small_prey_ratio = 0
        self.medium_prey_ratio = 0
        self.large_prey_ratio = 0

    def calculate_volumes(self):
        return {
            'low_vegetation_volume': int(self.size*self.low_vegetation_ratio*randint(80, 100)/100),
            'medium_vegetation_volume': int(self.size*self.medium_vegetation_ratio*randint(80, 100)/100),
            'high_vegetation_volume': int(self.size*self.high_vegetation_ratio*randint(60, 100)/100),
            'small_prey_volume': int(self.size*self.small_prey_ratio*randint(80, 100)/100),
            'medium_prey_volume': int(self.size*self.medium_prey_ratio*randint(80, 100)/100),
            'large_prey_volume': int(self.size*self.large_prey_ratio*randint(60, 100)/100)
        }

    # def calculate_volume(self):
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


class Arctic(Biome):

    def __init__(self, size):
        super().__init__(size)
        self.large_prey_ratio = 1
        self.medium_prey_ratio = 0.3
        self.small_prey_ratio = 0.2
        if size not in range(10, 101):
            raise Exception


biome1 = Arctic(100)

for i in range(3):
    print(biome1.calculate_volumes())
