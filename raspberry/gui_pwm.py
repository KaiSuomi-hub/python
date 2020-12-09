# pwm.py
from Tkinter import *
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 500)
pwm.start(100)


class App:

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        scale = Scale(frame, from_=0, to=100,
                      orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


root = Tk()
root.wm_title('PWM Power Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
