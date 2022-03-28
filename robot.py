import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os
import numpy as np


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body1.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK('brain' + str(solutionID) + '.nndf')
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system('rm brain' + str(solutionID) + '.nndf')

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Sense(self, i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            if jointName == 'Torso_BackLeg':
                self.motors[jointName] = MOTOR(jointName, self.amplitude, self.frequency, self.offset)
            else:
                self.motors[jointName] = MOTOR(jointName, self.amplitude, self.frequency, self.offset)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open('tmp' + str(self.solutionID) + '.txt', 'w')
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system('mv tmp' + str(self.solutionID) + '.txt fitness' + str(self.solutionID) + '.txt')
