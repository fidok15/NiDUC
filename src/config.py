import numpy as np
#python settings
RANDOM_SEED = None
#licza sygnałów
NUM_SENSORS = 3
#ustawienia wykresu
TIME = 5 * np.pi
STEP = 0.1
MOVE = 100
SCALE = 100
#zakłucenia
NORMAL_NOISE_STD = 2
FAULT_PROBABILITY = 0.5
LARGE_ERROR_BASE = 50.0
#liczba cykli monte carlo
N_CYCLES = 10000