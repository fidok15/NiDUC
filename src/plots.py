import matplotlib.pyplot as plt
import os
from src.config import ACCURACY_THRESHOLD, EPSILON, BETA

OUTPUT_DIR = "results"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def save_plot(title):
    """Helper function to save the current plot to disk."""
    # Delete unsupported signs
    safe_title = title.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "per").replace(":", "")
    filename = f"{OUTPUT_DIR}/{safe_title}.png"

    # Save in high resolution
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f" [INFO] Wykres zapisano: {filename}")


def plot_results(t, base_signal, signals, voted_output, stats, title):
    """
    Plots a single run timeline for visualization.
    """
    plt.figure(figsize=(12, 7))

    # Base signal (Truth)
    plt.plot(t, base_signal, label="Base Signal u(t)", color="black", linewidth=2, linestyle='--')

    # Sensors (Inputs)
    for i in range(signals.shape[0]):
        plt.plot(t, signals[i], label=f"Sensor {i + 1}", alpha=0.5, linewidth=1)

    # Voter Output (Result)
    plt.plot(t, voted_output, label="Voter Output", color="red", linewidth=2.5)

    plt.xlabel("Time (t)")
    plt.ylabel("Signal Value")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right')

    # Statistics Table (English)
    table_data = [
        ["Availability (nc/n)", f"{stats['availability_nc']:.4f}"],
        ["Safety (nic/n)", f"{stats['safety_nic']:.4f}"],
        ["Detection (nd/n)", f"{stats['detection_nd']:.4f}"],
        ["Correct Cycles", stats["correct"]],
        ["Incorrect Cycles", stats["incorrect"]],
        ["No Result Cycles", stats["unknown"]],
    ]

    plt.table(
        cellText=table_data,
        colLabels=["Metric", "Value"],
        cellLoc='center',
        loc='bottom',
        bbox=[0.15, -0.5, 0.7, 0.3],
    )
    plt.subplots_adjust(bottom=0.35)

    # --- Save to file ---
    save_plot(title)


    plt.show()


def plot_performance_curves(error_amplitudes, data_points, metric, title):
    """
    Plots performance curves comparing MAJ, SM, and WA.
    """
    plt.figure(figsize=(10, 6))

    metric_labels = {
        'nc': 'Availability (Normalized Correct Outputs)',
        'nic': 'Safety Failure Rate (Normalized Incorrect Outputs)',
        'nd': 'Detection Rate (Normalized Disagreed Outputs)',
    }

    # Plot lines
    plt.plot(error_amplitudes, data_points['Majority'][metric], label="MAJ (Majority)", linewidth=2, color='blue',
             marker='o', markersize=4)
    plt.plot(error_amplitudes, data_points['Smoothing'][metric], label="SM (Smoothing)", linewidth=3, color='green',
             linestyle='--', marker='s', markersize=4)
    plt.plot(error_amplitudes, data_points['Weighted'][metric], label="WA (Weighted Avg)", linewidth=1, color='gray',
             linestyle=':', alpha=0.7)

    plt.xlabel("Error Amplitude (e_max)")
    plt.ylabel(metric_labels.get(metric, metric))
    plt.title(f"{title}\n(Setup: Epsilon={EPSILON}, Beta={BETA})")
    plt.grid(True, alpha=0.3)
    plt.legend()

    save_plot(title)

