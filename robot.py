from weapon import Weapon
import random

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 150
               
    def set_weapon(self):
        self.active_weapon = input(f'Choose the Robots Weapon: Please Enter 1:Laser-Sword; 2:Photon-Baton; 3:Flame-Thrower \n')
        if self.active_weapon == '1':
            self.active_weapon = Weapon("Laser-Sword", random.randint(21, 61))
        elif self.active_weapon == '2':
            self.active_weapon = Weapon("Photon-Baton", random.randint(41, 51))
        elif self.active_weapon == '3':
            self.active_weapon = Weapon("Flame-Thrower", random.randint(11, 81))
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power