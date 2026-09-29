import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def get_triangle_wave_amplitude(freq, t):
    x = freq * t
    return 2.0 * np.abs(x - np.floor(x + 0.5))

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)