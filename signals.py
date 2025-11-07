import numpy as np
from scipy import signal

def generate_sine_wave(frequency,amplitude,phase,duration,sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    y = amplitude * np.sin(2*np.pi*frequency*t+phase)
    return t,y

def generate_sawtooth_wave(frequency,amplitude,phase,duration,sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    y = amplitude * signal.sawtooth(2*np.pi*frequency*t+phase)
    return t,y