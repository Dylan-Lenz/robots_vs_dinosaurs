from dinosaur import Dinosaur
import random

class Herd:
    
    def __init__(self):
        self.dino_herd = [Dinosaur('Rex', random.randint(21, 51)), Dinosaur('Stegs', random.randint(21, 51)), Dinosaur('Dak', random.randint(21, 51))]
         