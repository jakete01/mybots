import time
import os
import random
import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

amplitudeFront = np.pi / 8
frequencyFront = 18
phaseOffsetFront = 0
amplitudeBack = np.pi / 3
frequencyBack = 10
phaseOffsetBack = np.pi / 4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body1.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

targetAngleSinsFront = np.zeros(1000)
targetAnglesFront = np.linspace(0, np.pi*2, 1000)
for i in range(1000):
    targetAngleSinsFront[i] = amplitudeFront * np.sin(frequencyFront * targetAnglesFront[i] + phaseOffsetFront)

targetAngleSinsBack = np.zeros(1000)
targetAnglesBack = np.linspace(0, np.pi*2, 1000)
for i in range(1000):
    targetAngleSinsBack[i] = amplitudeBack * np.sin(frequencyBack * targetAnglesBack[i] + phaseOffsetBack)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

np.save(os.path.join('./data', 'targetAnglesFront.npy'), targetAngleSinsFront)
np.save(os.path.join('./data', 'targetAnglesBack.npy'), targetAngleSinsBack)

# exit()
for i in range(1000):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngleSinsBack[i], maxForce=500)

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngleSinsFront[i], maxForce=500)

    time.sleep(1/200)

np.save(os.path.join('./data', 'backLegSensorValues.npy'), backLegSensorValues)
np.save(os.path.join('./data', 'frontLegSensorValues.npy'), frontLegSensorValues)

p.disconnect()
