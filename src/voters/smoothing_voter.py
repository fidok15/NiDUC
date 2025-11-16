import numpy as np
from .base import Voter
from src.config import EPSILON, BETA


class SmoothingVoter():
    def __init__(self,epsilon = EPSILON, beta = BETA):
        self.epsilon = epsilon
        self.beta = beta
    
    def vote(self, sensor_values: np.ndarray):
        n = len(sensor_values)

        # do przegadania bo smoothing voter potrzebuje 
        # Odwołanie do pamięci: Algorytm pobiera ostatni poprzedni pomyślny wynik głosowania (oznaczony jako $X$)88.
        # tylko nasze probkowanie sygnalu ma mala wartosc czyli bysmy nwm musieli sprawdzac nwm 30 probek wstecz wartosci sygnalow, ajak to zrobic 