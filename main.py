# main.py - Monte Carlo Experiments

import numpy as np
import matplotlib.pyplot as plt

# Import necessary modules
from src.deafult import SignalGenerator
from src.noise import SensorArray
from src.calculations import calculate_statistics
from src.plots import plot_performance_curves, plot_results
from src.config import RANDOM_SEED, NUM_FAULT_SENSORS, NUM_SENSORS, LARGE_ERROR_BASE, ERROR_AMPLITUDES, \
    NUM_MONTE_CARLO_RUNS

# Import all Voter implementations
from src.voters.majority_voter import MajorityVoter
from src.voters.smoothing_voter import SmoothingVoter
from src.voters.weighted_voter import WeightedVoter


def run_single_simulation_cycle(voters, e_max):
    """
    Performs one complete simulation cycle (one run through the time array).
    Returns both statistics AND raw output signals.
    """

    # 1. Base Signal Generation
    base_gen = SignalGenerator()
    t, base_signal = base_gen.generate()

    # 2. Sensor Simulation and Error Injection (Sabotage)
    sensors_array = SensorArray(
        random_state=RANDOM_SEED,
        num_fault_sensors=NUM_FAULT_SENSORS,
        num_sensors=NUM_SENSORS,
        large_error_base=e_max  # Use the current e_max from the outer loop
    )
    signals = sensors_array.generate_signals(base_signal)

    # 3. Voting Loop (Time Iteration)
    results_stats = {}  # Stores dictionaries of statistics (nc, nic, nd)
    outputs_storage = {}  # Stores lists of raw voter outputs (for plotting)

    for name, voter_instance in voters.items():
        outputs = []
        # Loop through each time step (column)
        for i in range(signals.shape[1]):
            sensor_values = signals[:, i]
            outputs.append(voter_instance.vote(sensor_values))

        # Store raw outputs
        outputs_storage[name] = outputs

        # 4. Statistics Calculation
        results_stats[name] = calculate_statistics(base_signal, outputs)

    return results_stats, outputs_storage, t, base_signal, signals


def run_monte_carlo_experiments():
    """
    Performs the full Monte Carlo experiments.
    """

    # Structure to hold mean results for plotting curves
    data_points = {
        'Majority': {'nc': [], 'nic': [], 'nd': []},
        'Smoothing': {'nc': [], 'nic': [], 'nd': []},
        'Weighted': {'nc': [], 'nic': [], 'nd': []},
    }

    # Outer Loop: Iterates over Error Amplitude (e_max) - X-axis data
    for e_max in ERROR_AMPLITUDES:

        # Re-initialize voters for each new e_max test level
        voters = {
            'Majority': MajorityVoter(),
            'Smoothing': SmoothingVoter(),
            'Weighted': WeightedVoter(),
        }

        # Temporary storage for aggregation within this e_max run
        temp_stats = {name: {'nc': [], 'nic': [], 'nd': []} for name in voters.keys()}

        # Inner Loop: Monte Carlo Runs
        for run_id in range(NUM_MONTE_CARLO_RUNS):

            # !!! FIX: Unpack 5 values now, including outputs_storage !!!
            sim_stats, outputs_storage, t, base_signal, signals = run_single_simulation_cycle(voters, e_max)

            # Plot the very first run's timeline to verify logic visually
            if run_id == 0 and e_max == ERROR_AMPLITUDES[0]:
                # !!! FIX: Pass outputs_storage['Majority'] (list) as data, and sim_stats (dict) as table data
                plot_results(
                    t,
                    base_signal,
                    signals,
                    outputs_storage['Majority'],
                    sim_stats['Majority'],
                    title="Sample Timeline (MAJ) - Initial Run"
                )

            # Collect stats for averaging
            for name, stats in sim_stats.items():
                temp_stats[name]['nc'].append(stats['availability_nc'])
                temp_stats[name]['nic'].append(stats['safety_nic'])
                temp_stats[name]['nd'].append(stats['detection_nd'])

        # Aggregation: Calculate mean
        for name in voters.keys():
            data_points[name]['nc'].append(np.mean(temp_stats[name]['nc']))
            data_points[name]['nic'].append(np.mean(temp_stats[name]['nic']))
            data_points[name]['nd'].append(np.mean(temp_stats[name]['nd']))

        # Log progress (using Smoothing Voter safety as a sanity check)
        print(
            f"Finished Monte Carlo for E_max={e_max:.2f}. Avg. Safety (SM): {data_points['Smoothing']['nic'][-1]:.4f}")

    return data_points


if __name__ == "__main__":

    if NUM_FAULT_SENSORS < 2:
        print("WARNING: NUM_FAULT_SENSORS is set to 1. Change to 2 in config.py for meaningful trade-off analysis!")

    print(f"Starting Monte Carlo with {NUM_MONTE_CARLO_RUNS} runs per E_max level.")

    final_data = run_monte_carlo_experiments()

    # --- Generating Performance Curves ---

    # Plot 1: Availability
    plot_performance_curves(
        ERROR_AMPLITUDES,
        data_points=final_data,
        metric='nc',
        title="Availability (nc/n) vs. Error Amplitude"
    )

    # Plot 2: Safety (Catastrophic Failures)
    plot_performance_curves(
        ERROR_AMPLITUDES,
        data_points=final_data,
        metric='nic',
        title="Safety Failure Rate (nic/n) vs. Error Amplitude"
    )

    # Plot 3: Detection (Benign Failures)
    plot_performance_curves(
        ERROR_AMPLITUDES,
        data_points=final_data,
        metric='nd',
        title="Detection Rate (nd/n) vs. Error Amplitude"
    )

    plt.show()