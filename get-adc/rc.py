import time

import numpy as np
import RPi.GPIO as GPIO

import mcp3021_driver
import rc_fit

dynamic_range = 5.0    # опорное напряжение MCP3021, как в mcp.py
power_gpio = 14        # этим пином питаем RC-цепь

pre_time = 3.0         # сначала пишем разряженный конденсатор
charge_time = 100.0     # заряд
discharge_time = 80.0  # разряд

t_on = pre_time
t_off = pre_time + charge_time
t_end = t_off + discharge_time

GPIO.setmode(GPIO.BCM)
GPIO.setup(power_gpio, GPIO.OUT, initial=0)

adc = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []
power_values = []

try:
    start = time.time()

    while time.time() - start < t_end:
        t = time.time() - start
        state = 1 if t_on <= t < t_off else 0
        GPIO.output(power_gpio, state)

        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)
        power_values.append(state)

finally:
    GPIO.output(power_gpio, 0)
    GPIO.cleanup()
    adc.deinit()

# сырые данные сохраняем до подгонки
np.savetxt(
    "rc-data.csv",
    np.column_stack([time_values, voltage_values, power_values]),
    delimiter=",",
    header="t_s,U_V,power",
    comments="",
    fmt=["%.6f", "%.5f", "%d"],
)
print("Данные сохранены в rc-data.csv")

rc_fit.fit_and_plot(time_values, voltage_values, power_values, dynamic_range)