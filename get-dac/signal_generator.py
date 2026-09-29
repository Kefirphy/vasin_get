import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)