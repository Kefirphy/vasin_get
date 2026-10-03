import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(bit) for bit in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        max_number = 2 ** len(self.bits_gpio) - 1

        for number in range(max_number + 1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                return number

        return max_number

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / (2 ** len(self.bits_gpio) - 1) * self.dynamic_range

        if self.verbose:
            print(f"Число: {number}, напряжение: {voltage:.3f} В")

        return voltage

    def successive_approximation_adc(self):
        number = 0

        for bit in range(len(self.bits_gpio) - 1, -1, -1):
            number |= 1 << bit             
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                number &= ~(1 << bit)    

        return number

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        voltage = number / (2 ** len(self.bits_gpio) - 1) * self.dynamic_range

        if self.verbose:
            print(f"Число: {number}, напряжение: {voltage:.3f} В")

        return voltage


if __name__ == "__main__":
    adc = None
    try:
        adc = R2R_ADC(3.16)

        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.2f} В")

    finally:
        if adc is not None:
            adc.deinit()