from world import WORLD
from robot import ROBOT
import time
import pybullet_data
import pybullet as p


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI
        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == 'GUI':
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            if self.directOrGUI == 'GUI':
                time.sleep(1/1000)

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
