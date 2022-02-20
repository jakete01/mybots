from world import WORLD
from robot import ROBOT
import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim


class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

        self.world = WORLD()
        self.robot = ROBOT()


    def __del__(self):
        p.disconnect()


    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            time.sleep(1/200)
            self.robot.Sense(i)
            self.robot.Act(i)
