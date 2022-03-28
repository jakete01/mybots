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

    def Get_Weights(self):
        return self.weights

    def Evaluate(self, mode):
        # Generate all aspects of the simulation
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()

        # Call simulate.py from the command line
        os.system("python3 simulate.py " + mode + " " + str(self.myID) + " 2&>1 &")

        # Wait while the fitness file is not written to
        while not os.path.exists('fitness' + str(self.myID) + '.txt'):
            time.sleep(0.01)

        f = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(f.readline())
        f.close()

    def Create_Body(self):
        length = 1
        width = 1
        height = 1
        pyrosim.Start_URDF("body1.urdf")
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
        while not os.path.exists('body1.urdf'):
            time.sleep(0.01)


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
        pyrosim.Send_Sensor_Neuron(name=3, linkName='LeftLeg')
        pyrosim.Send_Sensor_Neuron(name=4, linkName='RightLeg')
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName='LowerFrontLeg')
        pyrosim.Send_Sensor_Neuron(name=7, linkName='LowerLeftLeg')
        pyrosim.Send_Sensor_Neuron(name=8, linkName='LowerRightLeg')

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=9, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='Torso_FrontLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_LeftLeg')
        pyrosim.Send_Motor_Neuron(name=12, jointName='Torso_RightLeg')
        pyrosim.Send_Motor_Neuron(name=13, jointName='BackLeg_LowerBackLeg')
        pyrosim.Send_Motor_Neuron(name=14, jointName='FrontLeg_LowerFrontLeg')
        pyrosim.Send_Motor_Neuron(name=15, jointName='LeftLeg_LowerLeftLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='RightLeg_LowerRightLeg')

        # Adding synapses to connect neurons
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
        while not os.path.exists('brain' + str(self.myID) + '.nndf'):
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
            time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * (c.numSensorNeurons - 1) - (c.numMotorNeurons - 1)

    def Set_ID(self, id):
        self.myID = id

    def Start_Simulation(self, mode):
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        os.system("python3 simulate.py " + mode + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_END(self):
        while not os.path.exists('fitness' + str(self.myID) + '.txt'):
            time.sleep(0.01)

        f = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(f.readline())
        f.close()
        print("Fitness of solution " + str(self.myID) + ": " + str(self.fitness))
        os.system('rm fitness' + str(self.myID) + '.txt')

    def Get_Fitness(self):
        return self.fitness
