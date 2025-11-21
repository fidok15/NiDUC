import numpy as np
from .base import Voter


class WeightedVoter(Voter):
    def vote(self, sensor_values: np.ndarray):
        n = len(sensor_values)
        
        # Obliczamy sumę odległości każdego czujnika od wszystkich innych
        # (Pairwise distances)
        total_distances = np.zeros(n)
        
        for i in range(n):
            # Dystans od i-tego czujnika do wszystkich pozostałych
            diffs = np.abs(sensor_values - sensor_values[i])
            total_distances[i] = np.sum(diffs)
        
        # Zabezpieczenie przed dzieleniem przez 0 (gdy wszystkie czujniki mają tę samą wartość)
        # Jeśli suma dystansów to 0, wszystkie wagi są równe
        with np.errstate(divide='ignore'):
            weights = 1.0 / (total_distances + 1e-6)
        
        # Normalizacja wag, aby sumowały się do 1.0
        weights_sum = np.sum(weights)
        if weights_sum == 0:
            # Fallback: średnia arytmetyczna, jeśli coś poszło nie tak
            return float(np.mean(sensor_values))
            
        normalized_weights = weights / weights_sum
        
        # Obliczenie średniej ważonej
        weightedSignal = float(np.sum(sensor_values * normalized_weights))

        return weightedSignal
