from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet

class Battlefield:

    def __init__(self):
        self.dinosaur = Herd().dino_herd[0]
        self.robot = Fleet().rob_fleet[0]

    def run_game(self):
        Battlefield().display_welcome()
        Battlefield().battle_phase()

    def display_welcome(self):
        print('\nWelcome to the Meat VS Metal Arena: \n')
    
    def battle_phase(self):
        while self.robot.health and self.dinosaur.health >= 0:
            self.robot.set_weapon()
            self.robot.attack_dinosaur(self.dinosaur)
            print(f'{self.dinosaur.name} is hit by {self.robot.name}, with an {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power}, making his health drop to {self.dinosaur.health}.')
            self.dinosaur.attack_robot(self.robot)
            print(f'{self.robot.name} is hit by {self.dinosaur.name} for {self.dinosaur.attack_power}, making his health drop to {self.robot.health}.\n')
            if self.dinosaur.health <= 1:
                print(f'The Champion is {self.robot.name}!!\n')
                return self.robot.name
            elif self.robot.health <= 1:
                print(f'The Champion is {self.dinosaur.name}!!\n')
                return self.dinosaur.name