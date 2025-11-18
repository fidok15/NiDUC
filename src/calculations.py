import numpy as np
from src.config import EPSILON

def calculate_statistics(base_signal, voted_output):
    n = len(base_signal)

    correct = 0
    incorrect = 0
    unknown = 0

    for i in range(n):
        v = voted_output[i]
        b = base_signal[i]

        # brak decyzji
        if v is None:
            unknown += 1
            continue

        # poprawna decyzja
        if abs(v - b) <= EPSILON:
            correct += 1
        else:
            incorrect += 1

    # normalizacja
    nc = correct / n
    nic = incorrect / n
    nd = unknown / n

    return {
        "availability_nc": nc,
        "safety_nic": nic,
        "detection_nd": nd,
        "total_cycles": n,
        "correct": correct,
        "incorrect": incorrect,
        "unknown": unknown,
    }
