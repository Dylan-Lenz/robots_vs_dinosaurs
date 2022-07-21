from weapon import Weapon
from dinosaur import Dinosaur
import random

class Robot:

    def __init__(self):
        self.name = 'Nator the Bot'
        self.health = 150
        self.active_weapon = Weapon('Axe', random.choices(range(21,51)))

    def attack_dinosaur(self, dinosaur):
        Dinosaur.health = dinosaur
        while dinosaur > 1:
            self.active_weapon.attack_power - dinosaur
            print(dinosaur)
            if dinosaur < 1:
                break