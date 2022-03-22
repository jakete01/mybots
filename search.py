import os
import parallelhc

os.system('rm brain*.nndf')
os.system('rm fitness*.txt')
phc = parallelhc.PARALLEL_HILL_CLIMBER()
phc.Evolve()

# for i in range(5):
#     os.system('python3 generate.py')
#     os.system('python3 simulate.py DIRECT')

