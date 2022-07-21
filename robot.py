from weapon import Weapon
import random

class Robot:

    def __init__(self):
        self.name = 'Nator the Bot'
        self.health = 150
        self.active_weapon = Weapon('Axe', random.choices(range(21,51))).name

""" R1 = Robot()
print(f'Name: {R1.name} Health :{R1.health} Weapon: {R1.active_weapon}') """