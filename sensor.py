import numpy as np
import pyrosim.pyrosim as pyrosim
import os


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)


    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == 999:
            print(self.values)


    def Save_Values(self):
        np.save(os.path.join('./data', self.linkName + 'SensorValues.npy'), self.values)
