class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 150
        self.attack_power = attack_power
        
    def attack_robot(self, robot):
        robot.health -= self.attack_power