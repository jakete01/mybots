import random
import time
import numpy as np
import os
import pyrosim.pyrosim as pyrosim


class SOLUTION:

    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Get_Weights(self):
        return self.weights

    def Evaluate(self, mode):
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        os.system("python3 simulate.py " + mode + " " + str(self.myID) + " &")

        while not os.path.exists('fitness.txt'):
            time.sleep(0.01)

        f = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(f.readline())
        print('Fitness: ' + str(self.fitness))
        f.close()

    def Create_Body(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 0.5
        pyrosim.Start_URDF("body1.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.End()
        while not os.path.exists('body1.urdf'):
            print('sleeping')
            time.sleep(0.01)

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
        pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')

        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
        while not os.path.exists('brain.nndf'):
            print('sleeping')
            time.sleep(0.01)

    def Create_World(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 0.5
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x - 10, y - 10, z], size=[length, width, height])
        pyrosim.End()

        while not os.path.exists('world.sdf'):
            print('sleeping')
            time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id

