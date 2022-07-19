""" 
(A)Create a new file for each class on the UML, as well as a main.py file that will serve as the entry point of your application.

(B)Fill in your classes from smallest to largest.
        (5pts)Make a class for each of the following: Robot, Dinosaur, Weapon, Battlefield.
    1)Weapon class
        (10pts)Weapon to have a name and attack_power. 
        (5pts)List of 3 possible weapons before a robot makes an attack. 
    2)Dinosaur class 
        (10pts)Dinosaur to have a name, health, and attack power.  
    3)Robot class 
        (10pts)Robot to have a name, health, and active_weapon. 
    4)Create Fleet and Herd classes 
        (5pts) List of 3 Robots to battle against a list of 3 Dinosaurs.

(C)Fill out the methods for your battle logic in the:
    -Battlefield class
        (10pts)Dinosaur to have the ability to attack a Robot on a Battlefield. 
            Method Lower a Robots health by the value of the Dinosaurs attack_power. 
        (10pts)Robot to have the ability to attack a Dinosaur on a Battlefield. 
            Method should lower the D's health by the attack_power of the R's active_weapon. 
        (10pts)Battle to conclude once either the robot or the dinosaur has its health points reduced to zero.

(D)Import the Dinosaur and Robot classes into the Battlefield class.

(E)Run the game by creating an object from the Battlefield class inside of main.py and calling the run_game method!
"""