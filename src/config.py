# config.py - Updated

import numpy as np

# Randomness Settings
RANDOM_SEED = None

# Number of Sensors (TMR)
NUM_SENSORS = 3
# Critical: Set to 2 or 3 to observe trade-offs (Double Error Injection)
NUM_FAULT_SENSORS = 2 

# Signal Parameters (u(t) = SCALE * sin(t) + MOVE)
TIME = 5 * np.pi
STEP = 0.1
MOVE = 100
SCALE = 100

# Error and Thresholds
# A_T (Accuracy Threshold): Used by the Comparator to check for correctness
ACCURACY_THRESHOLD = 0.5 
NORMAL_NOISE_STD = 0.5

# Error Range (e_max)
# This will be overridden by the Monte Carlo loop, but serves as a base range.
LARGE_ERROR_BASE = 10.0 
ERROR_SIZE_UP = 1.8
ERROR_SIZE_DOWN = 0.8

# Voters Thresholds
# Epsilon (Voter Threshold) - Used inside MAJ/SM to check variants agreement
EPSILON = 0.6 
# Beta (Smoothing Threshold) - Used by SM for temporal consistency
BETA = 0.6