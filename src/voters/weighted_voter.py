import numpy as np
from .base import Voter


class WeightedVoter(Voter):
    def vote(self, sensor_values: np.ndarray):
        median = np.median(sensor_values)
        #nie dizelimy przez 0 + 1e-6
        distances = np.abs(sensor_values - median) + 1e-6

        #odwrócenie wartości 
        weights = 1.0 / distances

        #normalizacaja
        weights = weights / np.sum(weights)

        weightedSignal = float(np.sum(sensor_values * weights))

        return weightedSignal
