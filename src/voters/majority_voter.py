import numpy as np
from .base import Voter
from src.config import EPSILON 

class MajorityVoter(Voter):
    def __init__(self, epsilon=EPSILON):
        self.epsilon = epsilon

    def vote(self, sensor_values: np.ndarray):
        #liczba czujnikow
        n = len(sensor_values)

        #wymagana większość  
        required = (n + 1) // 2
        sorted_values = np.sort(sensor_values)

        for i in range(n - required + 1):
            subset = sorted_values[i : i + required]
            
            if abs(subset[-1] - subset[0]) <= self.epsilon:
                return float(np.mean(subset))
            
        return None