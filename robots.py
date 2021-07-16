from weapons import Weapons

# Robots class


class Robots:
    ### Methods ###
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapons()  # calling weapons class

# method to have dinosaur attack robots
    def robot_attack(self, attack_dinosaur):
        # dinosaur loses health from robot attack depending on their weapons attack power.
        attack_dinosaur.health -= self.weapon.attack_power
