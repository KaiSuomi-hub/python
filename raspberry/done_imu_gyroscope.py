from sense_hat import SenseHat
import time
sense = SenseHat()
ledx = 4
ledy = 4
red = [255, 0, 0]
while True:
    try:
        sense.set_pixel(ledx, ledy, red)
        time.sleep(0.1)
        o = sense.get_orientation_degrees()
        p = o["pitch"]
        r = o["roll"]
        print("\rPitch: {:3.1f}, Roll: {:3.1f}".format(p, r), end=' ')

        if p > 5 and p < 50:
            if not ledx == 0:
                ledx = (ledx-1)

        if p < 355 and p > 310:
            if not ledx == 7:
                ledx = (ledx+1)

        if r > 5 and r < 50:
            if not ledy == 0:
                ledy = (ledy-1)

        if r < 355 and r > 310:
            if not ledy == 7:
                ledy = (ledy+1)

        sense.clear()

    except KeyboardInterrupt:
        print("\nDone!")
        sense.clear()
        exit()
