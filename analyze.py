import numpy
import matplotlib.pyplot

fitnessA = numpy.load('data/bestFitnessa.npy')
fitnessB = numpy.load('data/bestFitnessb.npy')


matplotlib.pyplot.plot(fitnessA, label='Fitness for Spot', linewidth=2)
matplotlib.pyplot.plot(fitnessB, label='Fitness for Quadruped', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
