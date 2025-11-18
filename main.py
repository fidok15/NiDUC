import matplotlib.pyplot as plt
from src.deafult import SignalGenerator
from src.noise import SensorArray
from src.config import NUM_SENSORS, RANDOM_SEED
from src.voters.majority_voter import MajorityVoter
from src.voters.weighted_voter import WeightedVoter
from src.voters.smoothing_voter import SmoothingVoter

from src.calculations import calculate_statistics
from src.plots import plot_results

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

    #dodanie szumu
    sensors = SensorArray(random_state=RANDOM_SEED)
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

    #wykresy
    plot_results(t, base_signal, signals, maj_output, stats_majority, title="Majority Voter")
    plot_results(t, base_signal, signals, wt_output, stats_weighted, title="Weighted Voter")
    plot_results(t, base_signal, signals, sm_output, stats_smoothing, title="Smoothing Voter")



if __name__ == "__main__":
    main()
