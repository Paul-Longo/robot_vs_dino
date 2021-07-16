from fleet import Fleet
from herd import Herd

# Battlefield class


class Battlefield:
    def __init__(self):
        self.dinosaur_herd = Herd()
        self.robot_fleet = Fleet()
        # display defeated opponents
        self.robot_defeated = []
        self.dinosaur_defeated = []

    # Methods
    def run_game(self):
        x = self.display_welcome()
        round = 1
        while len(self.herd.dinosaurs) or len(self. fleet.robot) > 0:
            print("Get ready to battle!")
            # If dinosaur is chosen. they will have first attack. else robot will have first attack
            if (x == "Dinosuars"):
                self.dino_turn(self)
                self.robo_turn(self)
                round += 1
            else:
                self.robo_turn(self)
                self.dino_turn(self)
                round += 1
        self.display_winners()
    # Print a welcome banner. Prompt user to choose a character(s). display their choice.

    def display_welcome(self):
        print(
            "Welcome to Robots vs Dinosaurs! This will be a fight to the death. Have Fun!")
        welcome_prompt = input("Do you want to be Robots or Dinosaurs")
        print(welcome_prompt + "Great choice! Let's Play!")

    def battle(self):
        print("Get ready to battle!")

# user will choose their dinosaur to battle with.
    def dino_turn(self):
        prompt_attack = input(
            "Choose your Dinosaur: dinosaur1, dinosaur2, dinosaur3")
        print(self.dinos_herd)
        if prompt_attack == 1:
            attacker = dinosaur1
            return attacker
        elif prompt_attack == 2:
            attacker = dinosaur2
            return attacker
        elif prompt_attack == 3:
            attacker = dinosaur3
            return attacker

    # user will choose their robot to battle with.

    def robo_turn(self):
        prompt_attack = input("Choose your robot: robot1, robot2, robot3")
        print(self.robot_fleet)
        if prompt_attack == 1:
            attacker = robot1
            return attacker
        elif prompt_attack == 2:
            attacker = robot2
            return attacker
        elif prompt_attack == 3:
            attacker = robot3
            return attacker

    def show_dino_opponent_options(self):
        print(self.robot_fleet)
        # user will be prompted to choose an opponent for their dinosaur to battle with.
        prompt_target = input("Choose your Opponent: robot1, robot2, robot3")
        print(self.robot_fleet)
        if prompt_target == 1:
            target = robot1
            return target
        elif prompt_target == 2:
            target = robot2
            return target
        elif prompt_target == 3:
            target = robot3
            return target
        # return target to defeated list
        if target.health <= 0:
            self.robot_defeated.append(target)

    def show_robo_opponent_options(self):
        print(self.dinosaur_herd)
        # user will choose an opponent to battle with
        prompt_target = input(
            "Choose your Opponent: dinosaur1, dinosaur2 dinosaur3")
        print(self.dinosaur_herd)
        if prompt_target == 1:
            target = dinosaur1
            return target
        elif prompt_target == 2:
            target = dinosaur2
            return target
        elif prompt_target == 3:
            target = dinosaur3
            return target
        # return target to defeated list
        if target.health < 0:
            self.dinosaur_defeated.append(target)

    def display_winners(self):
       # If the amount of robots is larger than the amount of dinosaurs left. Robots win. Else Dinosaurs win.
        if (len(self.dinosaur_herd > self.robot_fleet)):
            print("Dinosaurs are the Winner!")
        else:
            print("Robots are the winner")
