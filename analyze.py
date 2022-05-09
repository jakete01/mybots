import numpy
import matplotlib.pyplot

averageAValues = numpy.zeros(500)
averageBValues = numpy.zeros(500)

# Final Project Analysis
for i in range(2, 16):
    f1 = open('data/bestFitnessRun' + str(i) + 'a.npy', 'r')
    f2 = open('data/bestFitnessRun' + str(i) + 'b.npy', 'r')
    f1Lines = f1.readlines()
    f2Lines = f2.readlines()
    for j in range(0, 500):
        averageAValues[j] += float(f1Lines[j])
        averageBValues[j] += float(f2Lines[j])

for i in range(0, 500):
    averageAValues[i] = averageAValues[i] / 14
    averageBValues[i] = averageBValues[i] / 14

numpy.save('tempAveA.npy', averageAValues)
numpy.save('tempAveB.npy', averageBValues)

aveFitnessA = numpy.load('tempAveA.npy')
aveFitnessB = numpy.load('tempAveB.npy')


# Plot and show data
matplotlib.pyplot.title('Average fitness over 500 generations')
matplotlib.pyplot.plot(aveFitnessA, label='Recurrent Connections', linewidth=2)
matplotlib.pyplot.plot(aveFitnessB, label='No Recurrent Connections', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

print(averageBValues[0])
print(averageBValues[499])
