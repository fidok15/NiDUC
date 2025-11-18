import numpy as np
from .base import Voter
from src.config import EPSILON, BETA
from .majority_voter import MajorityVoter


class SmoothingVoter(Voter):
    """
    Algorithm Smoothing Voter (SM)
    Priority: The Availability-Safety Trade-off
    """

    def __init__(self, epsilon=EPSILON, beta=BETA):
        self.epsilon = epsilon
        self.beta = beta

        self.previous_vote = None

        self.maj_voter = MajorityVoter(epsilon=epsilon)

    def vote(self, sensor_values: np.ndarray):
        # Step 1: Check majority
        result_maj = self.maj_voter.vote(sensor_values)

        if result_maj is not None:
            # Majority found
            self.previous_vote = result_maj
            return result_maj

        # Step 2: Absence of majority. Begin smoothing
        if self.previous_vote is None:
            # In the first cycle (t=0), we take the median as the starting point if there is no majority.
            initial = float(np.median(sensor_values))
            self.previous_vote = initial
            return initial

        X = self.previous_vote

        # Step 3: Searching for the closest variant to the previous result.
        distances = np.abs(sensor_values - X)
        min_distance_index = np.argmin(distances)
        x_k = float(sensor_values[min_distance_index])
        d = distances[min_distance_index]

        # Step 4: Beta verification (smoothing)
        if d <= self.beta:
            self.previous_vote = x_k
            return x_k
        else:
            # Smoothing failed. Return None (No Result).
            return None