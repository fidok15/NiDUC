import numpy as np

# Ustawienia losowości
RANDOM_SEED = None

# Liczba czujników
NUM_SENSORS = 3

# Parametry sygnału
TIME = 5 * np.pi
STEP = 0.1
MOVE = 100
SCALE = 100

# Zakłócenia
NORMAL_NOISE_STD = 5
ERROR_SIZE_UP = 1.8
ERROR_SIZE_DOWN = 0.8
# liczba z przedziału <0,1>
FAULT_PROBABILITY = 0.2

LARGE_ERROR_BASE = 50.0

# Symulacja Monte Carlo
N_CYCLES = 10000
