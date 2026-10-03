import time

import r2r_adc
import adc_plot

dynamic_range = 3.16 

adc = r2r_adc.R2R_ADC(dynamic_range, compare_time=0.0001)

voltage_values = []
time_values = []
duration = 3.0

try:
    start = time.time()

    while time.time() - start < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - start)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()