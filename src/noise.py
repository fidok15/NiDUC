import numpy as np
from src.config import (
    NUM_SENSORS,
    NUM_FAULT_SENSORS,
    NORMAL_NOISE_STD,
    LARGE_ERROR_BASE,
    ERROR_SIZE_DOWN,
    ERROR_SIZE_UP,
)


class SensorArray:

    def __init__(
        self,
        num_sensors=NUM_SENSORS,
        num_fault_sensors=NUM_FAULT_SENSORS,
        normal_noise_std=NORMAL_NOISE_STD,
        large_error_base=LARGE_ERROR_BASE,
        random_state=None,
        error_size_down=ERROR_SIZE_DOWN,
        error_size_up=ERROR_SIZE_UP
    ):
        self.num_sensors = num_sensors
        self.num_fault_sensors = num_fault_sensors
        self.normal_noise_std = normal_noise_std
        self.large_error_base = large_error_base
        self.rng = np.random.default_rng(random_state)
        self.error_size_down = error_size_down
        self.error_size_up = error_size_up

    def generate_signals(self, base_signal: np.ndarray) -> np.ndarray:
        num_points = len(base_signal)
        sensors = np.zeros((self.num_sensors, num_points))
        num_to_fail = min(self.num_fault_sensors, self.num_sensors)
        
        faulty_indices = self.rng.choice(
            self.num_sensors, 
            size=num_to_fail, 
            replace=False
        )
        
        faulty_set = set(faulty_indices)

        for i in range(self.num_sensors):

            noisy_signal = base_signal + self.rng.normal(
                0, self.normal_noise_std, num_points
            )
            
            if i in faulty_set:
                start = self.rng.integers(0, num_points - num_points // 4)
                end = self.rng.integers(start + 10, num_points)
                error_magnitude = self.rng.choice([-1, 1]) * (
                    self.large_error_base * self.rng.uniform(self.error_size_down, self.error_size_up)
                )

                fault_length = end - start
                ramp = np.linspace(0, error_magnitude, fault_length)

                noisy_signal[start:end] += ramp
                noisy_signal[end:] += error_magnitude

            sensors[i, :] = noisy_signal

        return sensors
