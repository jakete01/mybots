import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os


class MOTOR:
    def __init__(self, jointName, amplitude, frequency, offset):
        self.jointName = jointName
        self.values = np.zeros(1000)
        self.amplitude = amplitude
        self.frequency = frequency
        self.offset = offset

        self.targetAngles = np.linspace(0, np.pi * 2, 1000)
        for i in range(1000):
            self.values[i] = self.amplitude * np.sin(self.frequency * self.targetAngles[i] + self.offset)


    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
                                    targetPosition=desiredAngle, maxForce=500)
