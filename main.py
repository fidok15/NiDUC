import matplotlib.pyplot as plt
from src.deafult import SignalGenerator
from src.noise import SensorArray
from src.config import NUM_SENSORS, RANDOM_SEED, NUM_ITERATION, LARGE_ERROR_BASE, ERROR_CHANGE
from src.voters.majority_voter import MajorityVoter
from src.voters.weighted_voter import WeightedVoter
from src.voters.smoothing_voter import SmoothingVoter
import pandas as pd
from src.calculations import calculate_statistics
from src.plots import plot_results
from src.summary_plots import plot_comparison
# uruchomienie voterow
def run_voter(voter, signals):
    outputs = []
    for i in range(signals.shape[1]):
        sensor_values = signals[:, i]
        result = voter.vote(sensor_values)
        outputs.append(result)
    return outputs
    
def main():
    #podstawowy sygnał
    base_gen = SignalGenerator()
    t, base_signal = base_gen.generate()

    results = []
    
    for i in range(NUM_ITERATION):
        error = LARGE_ERROR_BASE + (i * ERROR_CHANGE)
        #dodanie szumu
        sensors = SensorArray(random_state=RANDOM_SEED, large_error_base=error)
        signals = sensors.generate_signals(base_signal)

        # inicjalizacja voterow
        majority = MajorityVoter()
        weighted = WeightedVoter()
        smoothing = SmoothingVoter()

        #obliczenie funkcji voterow
        maj_output = run_voter(majority, signals)
        wt_output  = run_voter(weighted, signals)
        sm_output  = run_voter(smoothing, signals)

        #statystyka dla voterow
        stats_majority = calculate_statistics(base_signal, maj_output)
        stats_weighted = calculate_statistics(base_signal, wt_output)
        stats_smoothing = calculate_statistics(base_signal, sm_output)

        # wykresy
        # if i == 10 or i == NUM_ITERATION - 1:
        #     plot_results(t, base_signal, signals, maj_output, stats_majority, title="Majority Voter")
        #     plot_results(t, base_signal, signals, wt_output, stats_weighted, title="Weighted Voter")
        #     plot_results(t, base_signal, signals, sm_output, stats_smoothing, title="Smoothing Voter")

        #zapisanie do słownika
        results.append({
            'itteration': i,
            'current_error': error,
            'maj_nc': stats_majority['availability_nc'],
            'maj_nic': stats_majority['safety_nic'],
            'maj_nd': stats_majority['detection_nd'],
            'wt_nc': stats_weighted['availability_nc'],
            'wt_nic': stats_weighted['safety_nic'],
            'wt_nd': stats_weighted['detection_nd'],
            'sm_nc': stats_smoothing['availability_nc'],
            'sm_nic': stats_smoothing['safety_nic'],
            'sm_nd': stats_smoothing['detection_nd']
        })

    #wywołanie sumarczynych wykresów
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))
    plot_comparison(df_results)




if __name__ == "__main__":
    main()
