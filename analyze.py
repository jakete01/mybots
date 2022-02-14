import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')
targetAnglesFront = numpy.load('./data/targetAnglesFront.npy')
targetAnglesBack = numpy.load('./data/targetAnglesBack.npy')

# matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg Values', linewidth=4)
# matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg Values')

matplotlib.pyplot.plot(targetAnglesFront, label='Target Angles Front', linewidth=2)
matplotlib.pyplot.plot(targetAnglesBack, label='Target Angles Back', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
