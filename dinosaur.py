from weapon import Weapon
import random

class Dinosaur:

    def __init__(self):
        self.name = 'Zilla the Dino'
        self.health = 150
        self.attack_power = random.choices(range(21,51))

""" D1 = Dinosaur()
print(f'Name: {D1.name} Health :{D1.health}  Attack Power: {D1.attack_power}') """

