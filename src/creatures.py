from random import uniform


class Creature:
    pass

    def get_food_efficiency(self):
        return {
            'low_vegetation_volume': uniform(0, 1),
            'medium_vegetation_volume': uniform(0, 1),
            'high_vegetation_volume': uniform(0, 1),
            'small_prey_volume': uniform(0, 1),
            'medium_prey_volume': uniform(0, 1),
            'large_prey_volume': uniform(0, 1),
        }