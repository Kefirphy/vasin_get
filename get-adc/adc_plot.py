import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage, filename=None):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)

    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)

    plt.grid()

    if filename:
        plt.savefig(filename, dpi=150)

    plt.show()


def plot_sampling_period_hist(time, filename=None):
    sampling_periods = []

    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i - 1])

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)

    plt.title("Распределение периодов измерений")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")

    plt.xlim(0, 0.06)

    plt.grid()

    if filename:
        plt.savefig(filename, dpi=150)

    plt.show()