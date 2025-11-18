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
NORMAL_NOISE_STD = 0.5
#zakres naszego błędu 
ERROR_SIZE_UP = 1.8
ERROR_SIZE_DOWN = 0.8
#amplituda błędów
LARGE_ERROR_BASE = 10.0

#Voters
#próg głosujący 
EPSILON = 0.6
#próg wygładzający Smoothing voter
BETA = 0.6

#notatki 
# majority voter podnosi falge aby uzytkoniwk mogl wybrać safe state 
#co jak blad wystapi od chili 0 to smoothing voter nigdy nie bedzie mial parametru previous 
# if self.previous_vote is None: w smoothing do poprawy