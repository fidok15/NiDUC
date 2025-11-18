import matplotlib.pyplot as plt

def plot_results(t, base_signal, signals, voted_output, stats, title):

    plt.figure(figsize=(12, 7))

    # sygnał bazowy
    plt.plot(t, base_signal, label="Sygnał bazowy", color="black", linewidth=2)

    # czujniki
    for i in range(signals.shape[0]):
        plt.plot(t, signals[i], label=f"Czujnik {i+1}", alpha=0.6)

    # wynik głosowania
    plt.plot(t, voted_output, label="Wynik głosowania", color="red", linewidth=3)

    plt.xlabel("Czas")
    plt.ylabel("u(t)")
    plt.title(title)
    plt.grid(True)
    plt.legend(loc=1)

    table_data = [
        ["Dostępność (nc/n)", f"{stats['availability_nc']:.4f}"],
        ["Bezpieczeństwo (nic/n)", f"{stats['safety_nic']:.4f}"],
        ["Detekcja (nd/n)", f"{stats['detection_nd']:.4f}"],
        ["Liczba poprawnych", stats["correct"]],
        ["Liczba niepoprawnych", stats["incorrect"]],
        ["Braki decyzji", stats["unknown"]],
    ]

    plt.table(
        cellText=table_data,
        colLabels=["Metryka", "Wartość"],
        cellLoc='center',
        loc='bottom',
        bbox=[0.1, -0.7, 0.8, 0.4],
    )
    plt.subplots_adjust(bottom=0.25)
    plt.tight_layout()
    plt.show()
