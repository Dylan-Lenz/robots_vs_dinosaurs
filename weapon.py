import random

class Weapon:

    def _init_(self, weapon_names):
        self.weapon_name = weapon_names
        self.attack_power = random.choices(range(51))

    def weapon_names(self, weapon_names):
        weapon_names = ['Light-Saber', 'Fire-Staff', 'Stone-Hammer']
        self.weapon_name = weapon_names
    

