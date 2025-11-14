# import numpy as np
# from .base import Voter


# class WeightedAverageVoter(Voter):
#     def vote(self, sensor_values: np.ndarray) -> float:
#         median = np.median(sensor_values)
#         #nie dizelimy przez 0 + 1e-6
#         distances = np.abs(sensor_values - median) + 1e-6

#         weights = 1.0 / distances

#         #normalizacaja
#         weights = weights / np.sum(weights)

#         return float(np.sum(sensor_values * weights))


#TO DO ja to musze jeszcze ogarnać 