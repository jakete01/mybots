from simulation import SIMULATION
# targetAnglesFront = np.linspace(0, np.pi*2, 1000)
# for i in range(1000):
#     targetAngleSinsFront[i] = c.amplitudeFront * np.sin(c.frequencyFront * targetAnglesFront[i] + c.phaseOffsetFront)
#
# targetAngleSinsBack = np.zeros(1000)
# targetAnglesBack = np.linspace(0, np.pi*2, 1000)
# for i in range(1000):
#     targetAngleSinsBack[i] = c.amplitudeBack * np.sin(c.frequencyBack * targetAnglesBack[i] + c.phaseOffsetBack)
#
# np.save(os.path.join('./data', 'targetAnglesFront.npy'), targetAngleSinsFront)
# np.save(os.path.join('./data', 'targetAnglesBack.npy'), targetAngleSinsBack)

# np.save(os.path.join('./data', 'backLegSensorValues.npy'), backLegSensorValues)
# np.save(os.path.join('./data', 'frontLegSensorValues.npy'), frontLegSensorValues)


simulation = SIMULATION()
simulation.Run()
