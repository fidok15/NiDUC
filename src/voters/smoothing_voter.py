import numpy as np
from .base import Voter
from src.config import EPSILON, BETA

class SmoothingVoter(Voter):
    def __init__(self, epsilon=EPSILON, beta=BETA):
        self.epsilon = epsilon
        self.beta = beta
        self.previous_vote = None

    def vote(self, sensor_values: np.ndarray):
        # liczba czujników
        n = len(sensor_values)

        # wymagana większość
        required = (n + 1) // 2

        for i in range(n):
            group = [sensor_values[i]]

            # sprawdzamy każdy czujnik i dodajemy do grupy te których wartość leży w zakresie wartosc +/- epsilon
            for j in range(n):
                if i == j:
                    continue
                if abs(sensor_values[i] - sensor_values[j]) <= self.epsilon:
                    group.append(sensor_values[j])

            # sprawdzenie większości
            if len(group) >= required:
                result = float(np.mean(group))
                self.previous_vote = result  # zapisujemy poprawny wynik
                return result

        # jeśli jest to pierwszy cykl i nie ma poprzedniego wyniku nie można wygładzać
        # if self.previous_vote is None:
        #     # zwracamy medianę jako najlepsze pierwsze przybliżenie
        #     initial = float(np.median(sensor_values))
        #     self.previous_vote = initial
        #     return initial

        X = self.previous_vote  # ostatni poprawny wynik

        # szukamy najbliższego aktualnego pomiaru do poprzedniego wyniku
        distances = [abs(v - X) for v in sensor_values]
        k = int(np.argmin(distances))
        x_k = float(sensor_values[k])
        d = distances[k]

        # weryfikacja progu beta
        if d <= self.beta:
            # akceptujemy najbliższą wartość
            self.previous_vote = x_k
            return x_k

        return None
