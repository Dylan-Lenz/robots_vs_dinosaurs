import random

from robot import Robot

class Dinosaur:

    def __init__(self):
        self.name = 'Zilla the Dino'
        self.health = 150
        self.attack_power = random.choices(range(21,51))

    def attack_robot(self, robot):
        Robot.health = robot
        while robot > 1:
            self.attack_power - robot
            print(robot)
            if robot < 1:
                break
