# Herd class
from dinosaurs import Dinosaurs


class Herd:
    def __init__(self):
        self.dinosaurs = self.create_herd()  # creating a herd of dinoaurs

# names of dinos [Brney, Littlefoot, Bowser]
# setting each dinosaur equal to Dinosaur class. Adding a name, health, and attack power
# to be called into the Dinosar class.
    def create_herd(self):
        dinosaur1 = Dinosaurs()
        dinosaur1.name = "Barney"
        dinosaur1.health = 100
        dinosaur1.attack_power = 30

        dinosaur2 = Dinosaurs()
        dinosaur2.name = "Littlefoot"
        dinosaur2.health = 100
        dinosaur2.attack_power = 35

        dinosaur3 = Dinosaurs()
        dinosaur3.name = "Bowser"
        dinosaur3.health = 100
        dinosaur3.attack_power = 40

        # each dinosaur will be passed into the class Dinosaur with their name, health, and attack power.
        dinos = [dinosaur1, dinosaur2, dinosaur3]
        return dinos
