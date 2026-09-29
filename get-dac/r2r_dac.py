import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose=False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=max_voltage
        self.verbose=verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)

    def deinit(self):
        GPIO.out(self.gpio_bits,0)
        GPIO.cleanup()

    def voltage_to_number(self,voltage):
        if not (0.0<=self.voltage<=self.max_voltage):
            print(f"Напряжение выходит за ДД ЦАП (0.00-{self.max_voltage:.2f}) В")
            print("Устанавливаем 0.0В")
            return 0
        return int((self.voltage/self.max_voltage)*255)

    def set_voltage(self,number):
        GPIO.output(self.gpio_bits,[int(element) for element in bin(self.number)[2:].zfill(8)])

if __name__=="__main__":
    try:
        dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.183,True)

        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError():
                print("Неправильное число")
    finally:
        dac.deinit()