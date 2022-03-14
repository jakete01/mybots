import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5


def generate_robot():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x - 10, y - 10, z], size=[length, width, height])
    pyrosim.End()
    pyrosim.Start_URDF("body1.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()


def generate_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
    pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
    pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=0.3)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=0.1)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=0.4)
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=0.8)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=0.8)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=0.8)
    pyrosim.End()


generate_robot()
generate_brain()
