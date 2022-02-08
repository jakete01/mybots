import time
import os
import random
import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body1.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
for i in range(1000):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=-np.pi/4, maxForce=500)

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=np.pi/4, maxForce=500)

    time.sleep(1/200)

np.save(os.path.join('./data', 'backLegSensorValues.npy'), backLegSensorValues)
np.save(os.path.join('./data', 'frontLegSensorValues.npy'), frontLegSensorValues)

p.disconnect()
