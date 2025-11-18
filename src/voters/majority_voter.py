import numpy as np
from .base import Voter
from src.config import EPSILON


class MajorityVoter(Voter):
    """
    Algorithm Majority Voter (MAJ) for TMR (N=3).
    Priority: Safety. In absence of majority returns None
    """

    def __init__(self, epsilon=EPSILON):
        self.epsilon = epsilon

    def vote(self, sensor_values: np.ndarray):
        # Step 1: Sort input values (x1 <= x2 <= x3)
        sorted_values = np.sort(sensor_values)
        x1, x2, x3 = sorted_values[0], sorted_values[1], sorted_values[2]

        # Step 2: Check if majority exists

        # Check (x1, x2)
        if abs(x1 - x2) <= self.epsilon:
            # Majority found (x1, x2, (maybe x3))
            # Choose average value from group.
            return float((x1 + x2) / 2)

        # Check (x2, x3)
        if abs(x2 - x3) <= self.epsilon:
            # Majority found (x2, x3)
            # Return average
            return float((x2 + x3) / 2)

        # Step 3: Absence of majority.
        return None