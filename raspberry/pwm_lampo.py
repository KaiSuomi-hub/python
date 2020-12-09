# lampo.py
import spidev
import time
import RPi.GPIO as GPIO
led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)
# AO = 0, Al = 1, A2 = 2, A3 =3
temp_channel = 2
print("\nKytke liittimeen A%ld\n" % temp_channel)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


def readadc(adcnum):
    if adcnum > 3 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8+adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8)+r[2]
    return adcout


try:
    while True:
        value = readadc(temp_channel)
        volts = (value * 3.3) / 1024
        temperature_C = (volts - 0.5) * 100
        # katotaan mita value antaa ulos. Havaitaan etta 22.8c = 226
        # print(value)

        print("Jannitetaso = %5.3f V" % volts)
        print("%4.1f Celsiusastetta C" % temperature_C)
        print("--------------------------")
        # pyoristetaan ylos ja annetaan duty cyclelle prosentti value - 23 c * 10
        # * 10 jotta nahaan muutoksia
        base23 = abs((value-226)*10)
        # kytataan prosentteja
        print(base23)
        # annetaan prosentit
        # miksi useammalla rivilla, no jos ois kaksi ledia voisi vaihtaa varia vaikka siniseen kun on
        # alle 23 c
        duty_s = base23
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
        time.sleep(1)
finally:
    exit()
