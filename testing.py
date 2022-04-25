# File to run both tests in succession

import time
import os

start = time.perf_counter()
os.system('python3 search.py a')
time.sleep(2)
os.system('python3 search.py b')
end = time.perf_counter()

print('Elapsed time: ' + str(end - start) + ' seconds')
