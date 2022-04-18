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
        length = 1.8
        width = 0.8
        height = 0.4
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 2.25], size=[length, width, height])

        # Front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[-0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, -0.5, 0], size=[.2, .2, .5])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute",
                           position=[-0.1, -0.5, -0.25], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[-0.1, 0, -0.25], size=[.2, .2, .5])

        # Back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[.2, .2, .5])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",
                           position=[0.1, -0.5, -0.2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0.1, 0, -0.25], size=[.2, .2, .5])

        # Left Leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0, 0.5, 0], size=[.2, .2, .5])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute",
                           position=[-0.1, 0.5, -0.2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[-0.1, 0, -0.25], size=[.2, .2, .5])

        # Right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0, 0.5, 0], size=[.2, .2, .5])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute",
                           position=[0.1, 0.5, -0.2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0.1, 0, -0.25], size=[.2, .2, .5])


        # Arm
        pyrosim.Send_Joint(name='Torso_LowerArm', parent='Torso', child='LowerArm', type="revolute",
                           position=[-0.5, 0, 2.1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerArm", pos=[0, 0, 0.4], size=[.2, .2, 0.8])
        pyrosim.Send_Joint(name="LowerArm_UpperArm", parent="LowerArm", child="UpperArm", type="revolute",
                           position=[0, 0, 0.8], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="UpperArm", pos=[-0.4, 0, 0.1], size=[.8, .2, .2])
        # Fingers
        pyrosim.Send_Joint(name='UpperArm_TopFinger', parent='UpperArm', child='TopFinger', type="revolute",
                           position=[-0.8, 0, 0.1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="TopFinger", pos=[-0.2, 0, 0.1], size=[.4, .2, 0.1])
        pyrosim.Send_Joint(name="UpperArm_BottomFinger", parent="UpperArm", child="BottomFinger", type="revolute",
                           position=[-0.8, 0, -0.1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BottomFinger", pos=[-0.2, 0, 0.1], size=[.4, .2, .1])


        pyrosim.End()
        while not os.path.exists('body.urdf'):
            time.sleep(0.01)


    # Generates neural network, writes out to file
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName='LowerFrontLeg')
        pyrosim.Send_Sensor_Neuron(name=3, linkName='LowerLeftLeg')
        pyrosim.Send_Sensor_Neuron(name=4, linkName='LowerRightLeg')
        pyrosim.Send_Sensor_Neuron(name=5, linkName='UpperArm')
        pyrosim.Send_Sensor_Neuron(name=6, linkName='TopFinger')
        pyrosim.Send_Sensor_Neuron(name=7, linkName='BottomFinger')

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=8, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=9, jointName='Torso_FrontLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='Torso_LeftLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_RightLeg')
        pyrosim.Send_Motor_Neuron(name=12, jointName='BackLeg_LowerBackLeg')
        pyrosim.Send_Motor_Neuron(name=13, jointName='FrontLeg_LowerFrontLeg')
        pyrosim.Send_Motor_Neuron(name=14, jointName='LeftLeg_LowerLeftLeg')
        pyrosim.Send_Motor_Neuron(name=15, jointName='RightLeg_LowerRightLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='Torso_LowerArm')
        pyrosim.Send_Motor_Neuron(name=17, jointName='LowerArm_UpperArm')
        pyrosim.Send_Motor_Neuron(name=18, jointName='UpperArm_TopFinger')
        pyrosim.Send_Motor_Neuron(name=19, jointName='UpperArm_BottomFinger')

        # Adding synapses to connect neurons
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        # ---------------------
        # Linking leg sensors to motor neurons of arm
        # ---------------------

        # Toros_lowerArm
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=16, weight=self.weights[1][11])
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=16, weight=self.weights[2][11])
        pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=16, weight=self.weights[3][11])
        pyrosim.Send_Synapse(sourceNeuronName=4, targetNeuronName=16, weight=self.weights[4][11])

        # LowerArm_UpperArm
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=17, weight=self.weights[1][11])
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=17, weight=self.weights[2][11])
        pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=17, weight=self.weights[3][11])
        pyrosim.Send_Synapse(sourceNeuronName=4, targetNeuronName=17, weight=self.weights[4][11])

        # Fingers
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=18, weight=self.weights[1][11])
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=18, weight=self.weights[2][11])
        pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=18, weight=self.weights[3][11])
        pyrosim.Send_Synapse(sourceNeuronName=4, targetNeuronName=18, weight=self.weights[4][11])
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=19, weight=self.weights[1][11])
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=19, weight=self.weights[2][11])
        pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=19, weight=self.weights[3][11])
        pyrosim.Send_Synapse(sourceNeuronName=4, targetNeuronName=19, weight=self.weights[4][11])

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
        self.Create_Body()
        self.Create_World()
        os.system("python3 simulate.py " + mode + " " + str(self.myID) + " 2&>1 &")


    # Waits until simulation is done before writing out fitness to file
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists('fitness' + str(self.myID) + '.txt'):
            time.sleep(0.01)

        f = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(f.readline())
        f.close()
        print("Fitness of solution " + str(self.myID) + ": " + str(self.fitness))

        # Removes fitness file after use to avoid cluttering of directory
        os.system('rm fitness' + str(self.myID) + '.txt')