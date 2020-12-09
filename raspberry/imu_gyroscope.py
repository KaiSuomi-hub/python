from sense_hat import SenseHat
import time
sense = SenseHat()
ledx = 4
ledy = 4
red = [255,0,0]
while True:
      sense.set_pixel(ledx, ledy, red)
      time.sleep(0.1)
      asento = sense.get_orientation_degrees()

      p = asento["pitch"]
      r = asento["roll"]
      y = asento["yaw"]
      print("\rPitch: {:3.1f}, Roll: {:3.1f}, Yaw: {:3.1f}".format(p, r, y),end='')
      if p > 10 and p < 50:
         ledx = (ledx-1) % 8
      if p < 350 and p > 310:
         ledx = (ledx+1) % 8
      sense.clear()