# spcoord.py
from sense_hat import SenseHat
import time
import random
sense = SenseHat()


def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    c = [random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)]

    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            sense.set_pixel(abs(x-4), abs(y-4), c)
            time.sleep(0.05)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy


try:

    spiral(8, 8)
    sense.clear()
except KeyboardInterrupt:
    sense.clear()
