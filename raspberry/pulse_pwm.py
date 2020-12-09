# pwm.py
import time
import RPi.GPIO as GPIO
led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)
while True:
    for i in range(0, 100):
        duty_s = i
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
        time.sleep(0.1)
