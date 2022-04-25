# File to run both tests in succession

import time
import os

os.system('rm data/bestFitnessa.npy data/bestFitnessb.npy')
start = time.perf_counter()
os.system('python3 search.py a')
time.sleep(2)
os.system('python3 search.py b')
end = time.perf_counter()

print('Elapsed time: ' + str(end - start) + ' seconds')
