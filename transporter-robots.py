from random import random

from amak import AMAKPygame

from entities import RobotAgent
from system import TransporterRobotsEnvironment, TransporterRobotsMAS, GRID_WIDTH, GRID_HEIGHT

environment = TransporterRobotsEnvironment(room=1)
mas = TransporterRobotsMAS(environment)

for i in range(50):
    x = 0
    y = 0
    RobotAgent(mas, (x, y))

if __name__ == "__main__":
    AMAKPygame(mas, environment, GRID_WIDTH * 10, GRID_HEIGHT * 10, 120)
