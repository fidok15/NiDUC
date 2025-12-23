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

    def ramp(self, signal, start, end, error_magnitude, fault_length):
        
        ramp = np.linspace(0, error_magnitude, fault_length)
        signal[start:end] += ramp
        signal[end:] += error_magnitude
        return signal

    def drift(self, signal, start, end, error_magnitude, fault_length):
        

        # Łagodny dryf w kierunku błędu
        drift = np.cumsum(
            self.rng.normal(
                loc=error_magnitude / fault_length,
                scale=abs(error_magnitude) * 0.05,
                size=fault_length
            )
        )

        signal[start:end] += drift

        # po błędzie sygnał może wejść w offset lub wrócić częściowo
        if self.rng.random() < 0.5:
            post_offset = drift[-1]
        else:
            post_offset = error_magnitude * self.rng.uniform(0.3, 1.0)

        signal[end:] += post_offset

        return signal



    def generate_signals(self, base_signal: np.ndarray):
        num_points = len(base_signal)
        sensors = np.zeros((self.num_sensors, num_points))

        num_to_fail = min(self.num_fault_sensors, self.num_sensors)

        faulty_indices = self.rng.choice(
            self.num_sensors,
            size=num_to_fail,
            replace=False
        )

        for i in range(self.num_sensors):

            noisy_signal = base_signal + self.rng.normal(
                0, self.normal_noise_std, num_points
            )

            if i in faulty_indices:
                # losujemy moment błędu
                start = self.rng.integers(0, num_points - num_points // 4)
                end = self.rng.integers(start + 10, num_points)

                # losujemy kierunek i rozmiar błędu
                error_magnitude = self.rng.choice([-1, 1]) * (
                    self.large_error_base *
                    self.rng.uniform(self.error_size_down, self.error_size_up)
                )

                fault_length = end - start
                # wybór typu błędu
                error_type = self.rng.choice(
                    ["ramp", "drift"],
                    p=[0.5, 0.5]
                )

                if error_type == "ramp":
                    noisy_signal = self.ramp(noisy_signal, start, end, error_magnitude,fault_length)
                elif error_type == "drift":
                    noisy_signal = self.drift(noisy_signal, start, end, error_magnitude,fault_length)
                
                
            sensors[i, :] = noisy_signal

        return sensors