import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def generate_sine_wave(frequency,amplitude,phase,duration,sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    y = amplitude * np.sin(2*np.pi*frequency*t+phase)
    return t,y

def generate_sawtooth_wave(frequency,amplitude,phase,duration,sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    y = amplitude * signal.sawtooth(2*np.pi*frequency*t+phase)
    return t,y

def time_shift(t,y, shift):
    return t + shift, y

def time_scale(t, y, scale)
    return t * scale, y

def signal_addition(y1, y2):
    return y1 + y2

def signal_multiplication(y1, y2):
    return y1 * y2

def plot_signals(signals, labels=None, title="Signal Operation", xlabel="Time (s)", ylabel="Amplitude"):
    plt.figure(figsize=(8, 4))
    for i, (t, y) in enumerate(signals):
        label = labels[i] if labels else f"Signal {i+1}"
        plt.plot(t, y, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()