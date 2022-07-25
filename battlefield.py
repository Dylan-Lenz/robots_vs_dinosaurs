from herd import Herd
from fleet import Fleet
import random

class Battlefield:

    def __init__(self):
        self.dinosaur = Herd().dino_herd[random.randint(0, 2)]
        self.robot = Fleet().rob_fleet[random.randint(0, 2)]

    def run_game(self):
        Battlefield().display_welcome()
        Battlefield().battle_phase()

    def display_welcome(self):
        print('\nWELCOME TO MEAT & METAL ARENA!! \n')
    
    def battle_phase(self):
        while self.robot.health and self.dinosaur.health >= 0:
            self.robot.set_weapon()
            self.robot.attack_dinosaur(self.dinosaur)
            print(f'\n{self.dinosaur.name} the Dinosaur, is hit by {self.robot.name} the Robot with a {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power}, making his health drop to {self.dinosaur.health}.')
            self.dinosaur.attack_robot(self.robot)
            print(f'{self.robot.name} the Robot, is hit by {self.dinosaur.name} the Dinosaur for {self.dinosaur.attack_power}, making his health drop to {self.robot.health}.\n')
            if self.dinosaur.health <= 0:
                print(f'Metal Beats The Meat!\n{self.robot.name} the Robot Wins over {self.dinosaur.name} the Dinosaur!!\n')
                return self.robot.name
            elif self.robot.health <= 0:
                print(f'Meat Beats The Metal!\n{self.dinosaur.name} the Dinosaur Wins over {self.robot.name} the Robot!!\n')
                return self.dinosaur.name