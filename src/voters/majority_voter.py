import numpy as np
from .base import Voter


class MajorityVoter(Voter):

    def vote(self, sensor_values: np.ndarray) -> float:
        median = np.median(sensor_values)
        return float(median)
