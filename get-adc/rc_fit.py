import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def model(t, u_inf, u_start, tau):
    return u_inf + (u_start - u_inf) * np.exp(-t / tau)


def fit_phase(t, u):
    """Подбирает параметры экспоненты, возвращает (U_inf, U_нач, tau)."""
    params, _ = curve_fit(model, t, u, p0=[u[-1], u[0], 5.0])
    return params


def fit_and_plot(time_values, voltage_values, power_values, dynamic_range,
                 filename="rc-plot.png"):
    t = np.asarray(time_values)
    u = np.asarray(voltage_values)
    power = np.asarray(power_values)

    # границы фаз берём из столбца power
    i_on = np.argmax(power == 1)
    i_off = i_on + np.argmax(power[i_on:] == 0)
    t_on, t_off = t[i_on], t[i_off]

    p_ch = fit_phase(t[i_on:i_off] - t_on, u[i_on:i_off])
    p_dis = fit_phase(t[i_off:] - t_off, u[i_off:])

    print(f"Заряд:  U_inf = {p_ch[0]:.3f} В, tau = {p_ch[2]:.3f} с")
    print(f"Разряд: U_inf = {p_dis[0]:.3f} В, tau = {p_dis[2]:.3f} с")
    print(f"Среднее tau = {(p_ch[2] + p_dis[2]) / 2:.3f} с")

    # график: только измерения
    plt.figure(figsize=(10, 6))
    plt.plot(t, u)

    plt.title("Заряд и разряд конденсатора в RC-цепи")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(0, t.max())
    plt.ylim(0, dynamic_range)
    plt.grid()

    plt.savefig(filename, dpi=150)
    plt.show()


if __name__ == "__main__":
    data = np.loadtxt("rc-data.csv", delimiter=",", skiprows=1)
    fit_and_plot(data[:, 0], data[:, 1], data[:, 2], 5.0)