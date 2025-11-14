import matplotlib.pyplot as plt
from src.deafult import SignalGenerator
from src.noise import SensorArray
from src.config import NUM_SENSORS, RANDOM_SEED
from src.voters.majority_voter import MajorityVoter
from src.voters.weighted_voter import WeightedAverageVoter


def main():
    base_gen = SignalGenerator()
    t, base_signal = base_gen.generate()

    sensors = SensorArray(random_state=RANDOM_SEED)
    signals = sensors.generate_signals(base_signal)
    
    plt.figure(figsize=(10, 5))
    plt.plot(t, base_signal, label="Sygnał idealny", color="black", linewidth=2)

    for i in range(NUM_SENSORS):
        plt.plot(t, signals[i], label=f"Czujnik {i+1}", alpha=0.8)

    plt.xlabel("Czas [t]")
    plt.ylabel("u(t)")
    plt.title("Symulacja czujników z szumem i błędami grubymi")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
