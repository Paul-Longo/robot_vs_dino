# Wepons class
class Weapons:
    def __init__(self):
        self.weapon = ""  # setting weapon to an open string
        self.attack_power = 0  # setting power to 0

    # method to set attack power and name
    def set_name_and_attack(self, weapon, attack_power):
        self.weapon = weapon
        self.attack_power = attack_power


# spear will be the weapon and the attack power will be 30
spear = Weapons()
spear.set_name_and_attack("Spear", 30)
