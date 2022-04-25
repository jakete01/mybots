# Main executable, run to simulate as many generations and trials as specified in constants.py

import os
import sys
import parallelhc

testCase = sys.argv[1]
os.system('rm body.urdf')
os.system('rm brain*.nndf')
os.system('rm fitness*.txt')
phc = parallelhc.PARALLEL_HILL_CLIMBER(testCase)
phc.Evolve()
