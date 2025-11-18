import numpy as np
from .base import Voter


class WeightedVoter(Voter):
    """
    Algorithm Weighted Average (WA)
    """

    def vote(self, sensor_values: np.ndarray):
        median = np.median(sensor_values)

        # Step 1: Calculate distance from median
        distances = np.abs(sensor_values - median) + 1e-6

        # Step 2: Weights as inverse of distances
        weights = 1.0 / distances

        # Step 3: Weight normalisation and calculation of weighted average
        weights_norm = weights / np.sum(weights)

        weightedSignal = float(np.sum(sensor_values * weights_norm))

        return weightedSignal