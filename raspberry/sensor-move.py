import easygopigo3 as easy
import time


auto = easy.EasyGoPiGo3()
try:
    servo = auto.init_servo("SERVO1")
    for i in range(45, 135, 5):
        servo.rotate_servo(i)
        time.sleep(0.1)

finally:
    servo.reset_servo()
    time.sleep(1)
    servo.disable_servo()

auto = easy.EasyGoPiGo3()
etaisyysanturi = auto.init_distance_sensor()
kulkee = False
while True:
    #print("Etaisyys millimetreina: " + str(etaisyysanturi.read_mm()))
    # time.sleep(0.2)
    if kulkee and etaisyysanturi.read_mm() < 100:
        auto.stop()
        kulkee = False
        if not kulkee and etaisyysanturi.read_mm() > 100:
            auto.forward()
            kulkee = True
