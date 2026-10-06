import time

import mcp3021_driver
import adc_plot

dynamic_range = 5.0

adc = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []
duration = 10.0

try:
    start = time.time()

    while time.time() - start < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range, "mcp-plot.png")
    adc_plot.plot_sampling_period_hist(time_values, "mcp-hist.png")

finally:
    adc.deinit()