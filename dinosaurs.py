# Dinosaurs class
class Dinosaurs:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_power = 0

# method to have dinosaur attack robots
    def robot_attack(self, attack_robot):
        # robot loses health from dinosaur attack depending on their attack power.
        attack_robot.health -= self.attack_power
