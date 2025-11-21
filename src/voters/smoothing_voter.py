import numpy as np
from .base import Voter
from src.config import EPSILON, BETA

class SmoothingVoter(Voter):
    def __init__(self, epsilon=EPSILON, beta=BETA):
        self.epsilon = epsilon
        self.beta = beta
        self.previous_vote = None

    def vote(self, sensor_values: np.ndarray):
        n = len(sensor_values)
        required = (n + 1) // 2

        
        sorted_values = np.sort(sensor_values)
        
        for i in range(n - required + 1):
            subset = sorted_values[i : i + required]
            
            if abs(subset[-1] - subset[0]) <= self.epsilon:
                result = float(np.mean(subset))
                self.previous_vote = result
                return result

        #poprzedni jeśli jest to poprzedni cykl
        if self.previous_vote is None:
            initial = float(np.median(sensor_values))
            self.previous_vote = initial
            return initial

        X = self.previous_vote  # Poprzedni sukces

        distances = [abs(v - X) for v in sensor_values]
        k = int(np.argmin(distances))
        x_k = float(sensor_values[k])
        d = distances[k]

        if d <= self.beta:
            self.previous_vote = x_k
            return x_k

        return None
