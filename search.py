# Main executable, run to simulate as many generations and trials as specified in constants.py

import os
import parallelhc

os.system('rm brain*.nndf')
os.system('rm fitness*.txt')
phc = parallelhc.PARALLEL_HILL_CLIMBER()
phc.Evolve()

