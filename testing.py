# File to run both tests in succession

import time
import os

os.system('python3 search.py a')
time.sleep(2)
os.system('python3 search.py b')
