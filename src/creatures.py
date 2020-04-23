from enum import Enum
from random import randint, uniform

Proportion = Enum(
    'Proportion', 'GRACILE AGILE NORMAL BULKY HULKING'
)

#
# limbs: (forelimbs/hind limbs):
# length
# mobility
#
# resources:
# carrying
# power usage
#
# skin:
# thin, thick -> wet, scaled, hairy, furry
#
# internal organs:
# warm-bloodedness/cold-bloodedness
#
# carcass:
# frame (0-10)
# musculature (0-10)
#
# masticatory system:
# carnivore/omnivore/herbivore
# digestive system (0-10)
#
# brain:
# vision
# scent
# hearing
# coordination
# intellection


class Creature:

    def __init__(self, name, body_size ):
        self.name = name
        self.body_size = body_size

    def get_food_efficiency(self):
        return {
            'low_vegetation_volume': uniform(0, 1),
            'medium_vegetation_volume': uniform(0, 1),
            'high_vegetation_volume': uniform(0, 1),
            'small_prey_volume': uniform(0, 1),
            'medium_prey_volume': uniform(0, 1),
            'large_prey_volume': uniform(0, 1),
        }

    @property
    def weight(self):
        """0 to 10"""
        return 5

    @property
    def proportions(self):
        prop = self.weight - self.body_size
        if prop in range(-10, -5):
            return Proportion.GRACILE.value
        elif prop in range(-5, -2):
            return Proportion.AGILE.value
        elif prop in range(-2, 2):
            return Proportion.NORMAL.value
        elif prop in range(2, 5):
            return Proportion.BULKY.value
        elif prop in range(5, 11):
            return Proportion.HULKING.value
        else:
            raise IndexError

    def randomize_creature(self):
        """Creating randomized creature """
        main_params = {
            "name": self.name,
        }
        return {
            'main': main_params,
            'count': self.randomize_creature_countable_params(),
            'flag': self.randomize_creature_flag_params()
        }

    def randomize_creature_countable_params(self):
        """Randomize countable parameters"""
        return {
            "musculature": randint(0, 10),
            "frame": randint(0, 10),
        }

    def randomize_creature_flag_params(self):
        """Randomize flag parameters"""
        return {
            "warmblooded": 1
        }


class CreatureParameter:

    def __init__(self, name, stability, power_consumption):
        self.name = name
        self.stability = stability
        self.power_consumption = power_consumption


class RangedParameter(CreatureParameter):

    def __init__(self, name, value, stability, power_consumption):
        super().__init__(name, stability, power_consumption)
        self.value = value
