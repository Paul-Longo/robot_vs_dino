# Fleet class
from robots import Robots


class Fleet:
    def __init__(self):
        self.robots = self.create_fleet()

# Construct a fleet with names of each robot and health levels
    def create_fleet(self):
        robot1 = Robots()
        robot1.name = "T-100"
        robot1.health = 80

        robot2 = Robots()
        robot2.name = "wall-E"
        robot2.health = 75

        robot3 = Robots()
        robot3.name = "Megatronus Prime"
        robot3.health = 100

        robots = [robot1, robot2, robot3]
        return robots
