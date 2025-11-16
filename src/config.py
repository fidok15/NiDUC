import numpy as np

# Ustawienia losowości
RANDOM_SEED = None

# Liczba czujników
NUM_SENSORS = 3
# Liczba wadliwych czujników
NUM_FAULT_SENSORS = 1
# Parametry sygnału
TIME = 5 * np.pi
STEP = 0.1
MOVE = 100
SCALE = 100

# Zakłócenia
#A_T
NORMAL_NOISE_STD = 5
#zakres naszego błędu 
ERROR_SIZE_UP = 1.8
ERROR_SIZE_DOWN = 0.8
#maksymalna amplituda błędów
LARGE_ERROR_BASE = 50.0

#Voters
#próg głosujący 
EPSILON = 0.1
#próg wygładzający Smoothing voter
BETA = 0.1

#notatki 
# majority voter podnosi falge aby uzytkoniwk mogl wybrać safe state 