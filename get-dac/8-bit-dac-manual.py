import RPi.GPIO as GPIO

dac_bits=[16,20,21,25,26,17,27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits,GPIO.OUT)

max_voltage=3.3

def voltage_to_number(voltage):
    if not (0.0<=voltage<=max_voltage):
        print(f"Напряжение выходит за ДД ЦАП (0.00-{max_voltage:.2f}) В")
        print("Устанавливаем 0.0В")
        return 0
    return int((voltage/max_voltage)*255)

def number_to_dac(number):
    GPIO.output(dac_bits,[int(element) for element in bin(number)[2:].zfill(8)])

try:
    while True:
        try:
            voltage=float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)  
            number_to_dac(number)         
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз \n")
finally:
    GPIO.output(dac_bits,0)
    GPIO.cleanup()

