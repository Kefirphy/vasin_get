import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2             
signal_frequency = 10       
sampling_frequency = 1000   

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5.0, verbose=False)

        start_time = time.time()

        while True:
            current_time = time.time() - start_time
            norm_value = sg.get_sin_wave_amplitude(signal_frequency, current_time)
            target_voltage = norm_value * amplitude
            
            dac.set_voltage(target_voltage)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()