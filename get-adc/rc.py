import time

import mcp3021_driver
import adc_plot

dynamic_range = 5.0  # то же значение, что и в mcp.py

adc = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []
duration = 10.0  # подберите под свою цепь, см. ниже

try:
    print("Измерение началось: через 1-2 с нажмите и отпустите кнопку разряда")
    start = time.time()

    while time.time() - start < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range, "rc-plot.png")

finally:
    adc.deinit()