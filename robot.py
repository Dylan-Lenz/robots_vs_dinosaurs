from weapon import Weapon
import random

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = Weapon("Axe", random.randint(21, 51))
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power