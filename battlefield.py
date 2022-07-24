from herd import Herd
from fleet import Fleet

class Battlefield:

    def __init__(self):
        self.dinosaur = Herd().dino_herd[0]
        self.robot = Fleet().rob_fleet[0]
        pass

    def run_game(self):
        Battlefield()

    def welcome(self):
        self.welcome = print('Welcome')
      
    def battle_phase(self):
        while self.robot.health and self.dinosaur.health >= 0:
            self.robot.attack_dinosaur(self.dinosaur)
            print(f'{self.dinosaur.name} is hit by {self.robot.name} for {self.robot.active_weapon.attack_power}, making his health now {self.dinosaur.health}.')
            #print('')
            self.dinosaur.attack_robot(self.robot)
            print(f'{self.robot.name} is hit by {self.dinosaur.name} for {self.dinosaur.attack_power}, making his health now {self.robot.health}.')
            print('')
            if self.dinosaur.health <= 1:
                return self.robot.name
            elif self.robot.health <= 1:
                return self.dinosaur.name
                
    def display_winner(self):
        self.display_winner = (f'The winner is:') 
      
B1 = Battlefield()
print(B1.battle_phase())
                

            
                