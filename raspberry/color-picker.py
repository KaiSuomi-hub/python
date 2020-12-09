# color-picker.py
from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import numpy as np

r = 200
g = 200
b = 200

sense = SenseHat()

w = np.array([r, g, b])

a = 0

square = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
]

# painallus vaihtaa ledi-varia jota muutetaan (w[array indeksi])


def pushed_middle(event):
    global a
    if event.action != ACTION_RELEASED:
        if a < 3:
            a += 1
        if a > 2:
            a = 0
        print("Working with:", w[a])


def pushed_up(event):
    global w
    if event.action != ACTION_RELEASED:
        w[a] += 5
        if w[a] == 255:
            w[a] = 0
        print("Up", w[a])
        print(w)


def pushed_down(event):
    global w
    if event.action != ACTION_RELEASED:
        w[a] -= 5
        if w[a] == 0:
            w[a] = 255
        print("Down", w[a])
        print(w)


# printataan rgb
def pushed_left(event):
    if event.action != ACTION_RELEASED:
        sense.show_message(f"R: {w[0]}, G: {w[1]}, B: {w[2]}", text_colour=[
                           255, 255, 255], back_colour=[0, 0, 0])
        refresh()

# printataan hex


def pushed_right(event):
    if event.action != ACTION_RELEASED:
        sense.show_message(f"{''.join('{:02x}'.format(x) for x in w)}", text_colour=[
                           255, 255, 255], back_colour=[0, 0, 0])


def refresh():
    sense.clear()
    sense.set_pixels(square)


try:
    while True:
        sense.stick.direction_up = pushed_up
        sense.stick.direction_down = pushed_down
        sense.stick.direction_left = pushed_left
        sense.stick.direction_right = pushed_right
        sense.stick.direction_middle = pushed_middle
        sense.stick.direction_any = refresh
        refresh()
        pause()

except KeyboardInterrupt:
    print("\nExiting")
    sense.show_message(f"BYE!", text_colour=[
        255, 255, 255], back_colour=[0, 0, 0])
    sense.clear()
