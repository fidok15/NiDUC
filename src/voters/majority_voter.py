import numpy as np
from .base import Voter
from src.config import EPSILON 

class MajorityVoter(Voter):
    def __init__(self, epsilon=EPSILON):
        self.epsilon = epsilon

    def vote(self, sensor_values: np.ndarray):

        n = len(sensor_values)

        required = (n + 1) // 2

        consistent_values = []

        for i in range(n):
            group = [sensor_values[i]]

            for j in range(n):
                if i == j:
                    continue
                if abs(sensor_values[i] - sensor_values[j]) <= self.epsilon:
                    group.append(sensor_values[j])

            if len(group) >= required:
                return float(np.mean(group))

        majoritySignal = float(np.median(sensor_values))

        return majoritySignal
