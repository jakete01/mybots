import time

import pybullet as p

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for x in range(1000):
    p.stepSimulation()
    print(x)
    time.sleep(1/60)

p.disconnect()

