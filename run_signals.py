"""
run_signals.py
Generates multiple signals using functions from signals.py,
performs basic operations, and saves all results to text files.
"""

import numpy as np
from signals import (generate_sine_wave,generate_sawtooth_wave,time_shift,time_scale,signal_addition,signal_multiplication)


def run_signals():
    """Generate, modify, and save multiple signals to .txt files."""
    #generate base signals
    t1, y1 = generate_sine_wave(frequency=5, amplitude=1.0, phase=0, duration=1, sampling_rate=1000)
    t2, y2 = generate_sawtooth_wave(frequency=5, amplitude=0.7, phase=0, duration=1, sampling_rate=1000)

    # perorm operations
    t_shifted, y_shifted = time_shift(t1, y1, shift=0.1)
    t_scaled, y_scaled = time_scale(t1, y1, scale=1.5)
    y_sum = signal_addition(y1, y2)
    y_prod = signal_multiplication(y1, y2)

    #plot all signals in a single plot
    plot_signals([(t1, y1),(t_shifted, y_shifted),(t_scaled, y_scaled),(t1, y_sum),(t1, y_prod)],labels=["Original Sine Wave","Time Shifted","Time Scaled",
            "Signal Addition","Signal Multiplication"],title="All Generated Signals")

    save_signal("time_shifted.txt", t_shifted, y_shifted)
    save_signal("time_scaled.txt", t_scaled, y_scaled)
    save_signal("signal_addition.txt", t1, y_sum)
    save_signal("signal_multiplication.txt", t1, y_prod)

    print("All signals saved as .txt files.")


def save_signal(filename, t, y):
    """Save a signal’s time and amplitude values to a text file."""
    data = np.column_stack((t, y))
    np.savetxt(filename, data, fmt="%.6f", header="Time(s)\tAmplitude", comments="")
    print(f"💾 Saved: {filename}")


if __name__ == "__main__":
    run_signals()

