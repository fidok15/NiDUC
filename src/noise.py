import numpy as np
from src.config import (
    NUM_SENSORS, NORMAL_NOISE_STD,
    FAULT_PROBABILITY, LARGE_ERROR_BASE
)


def generate_sensor_signals(base_signal: np.ndarray, random_state: int) -> np.ndarray:
    rng = np.random.default_rng(random_state)
    num_points = len(base_signal)
    sensors = np.zeros((NUM_SENSORS, num_points))
    print(len(base_signal))
    
    for i in range(NUM_SENSORS):
        noisy_signal = base_signal + rng.normal(0, NORMAL_NOISE_STD, num_points)
        
        # Czy ten czujnik dostanie błąd gruby?
        if rng.random() < FAULT_PROBABILITY:
            start = rng.integers(0, num_points - num_points // 4)
            end = rng.integers(start + 10, num_points)
            error_magnitude = rng.choice([-1, 1]) * (
                LARGE_ERROR_BASE * rng.uniform(0.8, 1.2)
            )

            fault_length = end - start
            ramp = np.linspace(0, error_magnitude, fault_length)

            noisy_signal[start:end] += ramp
            noisy_signal[end:] += error_magnitude

            print(f"[FAULT] Sensor {i} – gruby błąd (rampa) od {start} do {end}, Δ={error_magnitude:.2f}")

        sensors[i, :] = noisy_signal

    return sensors
