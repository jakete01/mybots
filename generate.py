import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

for j in range(2):
    x += j
    y = 0
    for h in range(2):
        y += h
        length = 1
        width = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z + i], size=[length, width, height])
            length *= .9
            width *= .9

pyrosim.End()