import random
import time
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import constants as c


class SOLUTION:

    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * (c.numSensorNeurons - 1) - (c.numMotorNeurons - 1)


    # --------------------
    # Generation functions
    # --------------------

    # Creates robot body, writes out to file
    def Create_Body(self):
        length = 1
        width = 1
        height = 1
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])

        # Front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, .5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Left Leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.End()
        while not os.path.exists('body.urdf'):
            time.sleep(0.01)


    # Generates neural network, writes out to fil e
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeftLeg')
        pyrosim.Send_Sensor_Neuron(name=3, linkName='BackRightLeg')
        pyrosim.Send_Sensor_Neuron(name=4, linkName='FrontRightLeg')
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerBackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName='LowerFrontLeftLeg')
        pyrosim.Send_Sensor_Neuron(name=7, linkName='LowerBackRightLeg')
        pyrosim.Send_Sensor_Neuron(name=8, linkName='LowerFrontRightLeg')

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=9, jointName='Torso_BackLeftLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='Torso_FrontLeftLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_FrontRightLeg')
        pyrosim.Send_Motor_Neuron(name=12, jointName='Torso_BackRightLeg')
        pyrosim.Send_Motor_Neuron(name=13, jointName='BackLeftLeg_LowerBackLeftLeg')
        pyrosim.Send_Motor_Neuron(name=14, jointName='FrontLeftLeg_LowerFrontLeftLeg')
        pyrosim.Send_Motor_Neuron(name=15, jointName='BackRightLeg_LowerBackRightLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='FrontRightLeg_LowerFrontRightLeg')

        # Adding synapses to connect neurons
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
        while not os.path.exists('brain' + str(self.myID) + '.nndf'):
            time.sleep(0.01)


    # Generates body for spot dog robot
    def Create_Spot_Body(self):
        length = 2
        width = .8
        height = 1
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 2], size=[length, width, height])

        # Front left leg
        pyrosim.Send_Joint(name="Torso_FrontLeftLeg", parent="Torso", child="FrontLeftLeg", type="revolute",
                           position=[-0.5, .5, 1.5], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-0.5, 0, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeftLeg_LowerFrontLeftLeg", parent="FrontLeftLeg", child="LowerFrontLeftLeg",
                           type="revolute", position=[-0.5, 0, -1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Back left leg
        pyrosim.Send_Joint(name="Torso_BackLeftLeg", parent="Torso", child="BackLeftLeg", type="revolute",
                           position=[-0.5, -0.5, 1.5], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[0.5, 0, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeftLeg_LowerBackLeftLeg", parent="BackLeftLeg", child="LowerBackLeftLeg",
                           type="revolute", position=[-0.5, 0, -1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeftLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Front right Leg
        pyrosim.Send_Joint(name="Torso_FrontRightLeg", parent="Torso", child="FrontRightLeg", type="revolute",
                           position=[0.5, 0.5, 1.5], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="FrontRightLeg_LowerFrontRightLeg", parent="FrontRightLeg", child="LowerFrontRightLeg",
                           type="revolute", position=[0.5, 0, -1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerFrontRightLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Back Right leg
        pyrosim.Send_Joint(name="Torso_BackRightLeg", parent="Torso", child="BackRightLeg", type="revolute",
                           position=[0.5, -0.5, 1.5], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="BackRightLeg_LowerBackRightLeg", parent="BackRightLeg", child="LowerBackRightLeg",
                           type="revolute", position=[0.5, 0, -1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerBackRightLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.End()
        while not os.path.exists('body.urdf'):
            time.sleep(0.01)

    # Generates brain for spot dog robot
    def Create_Spot_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")


        # Adding synapses to connect neurons
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
        while not os.path.exists('brain' + str(self.myID) + '.nndf'):
            time.sleep(0.01)

    # Generates world elements, writes out to file
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
            time.sleep(0.01)


    # Returns this solutions fitness value
    def Get_Fitness(self):
        return self.fitness


    # Returns this solution's matrix of synaptic weights
    def Get_Weights(self):
        return self.weights


    # Randomly changes one of the synaptic weights
    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * (c.numSensorNeurons - 1) - (c.numMotorNeurons - 1)


    # Sets this solutions ID
    def Set_ID(self, id):
        self.myID = id


    # Gives OS call to start the simulation for this solution
    def Start_Simulation(self, mode):
        self.Create_Brain()
        # self.Create_Body()
        self.Create_World()
        # self.Create_Spot_Brain()
        self.Create_Spot_Body()
        os.system("python3 simulate.py " + "GUI" + str(self.myID) + " 2&>1 &")


    # Waits until simulation is done before writing out fitness to file
    def Wait_For_Simulation_To_END(self):
        while not os.path.exists('fitness' + str(self.myID) + '.txt'):
            time.sleep(0.01)

        f = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(f.readline())
        f.close()
        print("Fitness of solution " + str(self.myID) + ": " + str(self.fitness))

        # Removes fitness file after use to avoid cluttering of directory
        os.system('rm fitness' + str(self.myID) + '.txt')
