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

        for i in range(n):
            group = [sensor_values[i]]
            
            #sprawdzamy kazdy czujnik i dodajemy do grupy te ktorych wartosc lezy w zakresie wartosc +/- alfa 
            for j in range(n):
                if i == j:
                    continue
                if abs(sensor_values[i] - sensor_values[j]) <= self.epsilon:
                    group.append(sensor_values[j])

            #sprawdzenie większości
            if len(group) >= required:
                return float(np.mean(group))
        #zwrocenie mediany z grupy poprawnych 
        majoritySignal = float(np.median(sensor_values))

        return majoritySignal
