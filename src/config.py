import numpy as np

# Ustawienia losowości
RANDOM_SEED = 1

# Liczba czujników
NUM_SENSORS = 3
# Liczba wadliwych czujników
NUM_FAULT_SENSORS = 3
# Parametry sygnału
TIME = 5 * np.pi
STEP = 0.1
MOVE = 100
SCALE = 100

# Zakłócenia
#A_T
NORMAL_NOISE_STD = 0.001
#zakres naszego błędu 
ERROR_SIZE_UP = 1
ERROR_SIZE_DOWN = 1
#amplituda błędów
LARGE_ERROR_BASE = 0
ERROR_CHANGE = 1
NUM_ITERATION = 100
#Voters
#próg głosujący 
EPSILON = 0.5
#próg wygładzający Smoothing voter
BETA = 1

#notatki 
# majority voter podnosi falge aby uzytkoniwk mogl wybrać safe state 
#co jak blad wystapi od chili 0 to smoothing voter nigdy nie bedzie mial parametru previous 
# if self.previous_vote is None: w smoothing do poprawy