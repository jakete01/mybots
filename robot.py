import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os


class ROBOT:


    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK('brain' + str(solutionID) + '.nndf')
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system('rm brain' + str(solutionID) + '.nndf')


    # Sends motor values to the motors, causing the robot to move
    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)


    # Calculates and returns this robots fitness value
    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        f = open('tmp' + str(self.solutionID) + '.txt', 'w')
        f.write(str(xPosition))
        f.close()
        os.system('mv tmp' + str(self.solutionID) + '.txt fitness' + str(self.solutionID) + '.txt')


    # Prepares the motor neurons and motors to move
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


    # Prepares sensors to work properly
    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    # Updates the sensor values from the current time step
    def Sense(self, i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)


    # Updates the neural network to change any synapse values necessary
    def Think(self):
        self.nn.Update()

