# Wepons class
class Weapons:
    def __init__(self):
        self.weapon = ""
        self.attack_power = 0

    def set_name_and_attack(self, weapon, attack_power):
        self.weapon = weapon
        self.attack_power = attack_power


spear = Weapons()
spear.set_name_and_attack("Spear", 30)
