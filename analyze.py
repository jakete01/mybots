import numpy
import matplotlib.pyplot

f = open('data/bestFitnessa.npy', 'r')
runA = numpy.zeros(200)
lines = f.readlines()
for i in range(0, len(lines)):
    runA[i] = float(lines[i])
numpy.save('tempA.npy', runA)

f = open('data/bestFitnessb.npy', 'r')
runB = numpy.zeros(200)
lines = f.readlines()
for i in range(0, len(lines)):
    runB[i] = float(lines[i])
numpy.save('tempB.npy', runB)

fitnessA = numpy.load('tempA.npy')
fitnessB = numpy.load('tempB.npy')


matplotlib.pyplot.plot(fitnessA, label='Fitness: Recurrent Connections', linewidth=2)
matplotlib.pyplot.plot(fitnessB, label='Fitness: No Recurrent Connections', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
