import matplotlib.pyplot as plt
from src.deafult import generate_base_signal
from src.noise import generate_sensor_signals
from src.config import NUM_SENSORS, RANDOM_SEED

def main():
    t, base_signal = generate_base_signal()
    sensors = generate_sensor_signals(base_signal, RANDOM_SEED)

    plt.figure(figsize=(10, 5))
    plt.plot(t, base_signal, label="Sygnał idealny", color="black", linewidth=2)

    for i in range(NUM_SENSORS):
        plt.plot(t, sensors[i], label=f"Czujnik {i+1}", alpha=0.8)

    plt.xlabel("Czas [t]")
    plt.ylabel("u(t)")
    plt.title("Symulacja czujników z szumem i błędami grubymi")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
