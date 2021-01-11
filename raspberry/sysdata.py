import psutil
import datetime
import time     # import the time library for the sleep function
from easygopigo3 import EasyGoPiGo3
import shutil
from gpiozero import CPUTemperature
gpg = EasyGoPiGo3()
volt = '{0:.3g}'. format(gpg.volt())
ram = '{0:.3g}'. format(psutil.virtual_memory().available * 100 /
                        psutil.virtual_memory().total)
disk = shutil.disk_usage("/")
temp = CPUTemperature()
tiedosto = open("stats.txt", "a")
with open("stats.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass

print("Edelliset lukemat:", last_line)
aika = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M')
data = aika, "Volt:", volt, "Ram % free:", ram, "Disk /:", disk, "Temp:", temp.temperature, "\n"
tiedosto.write(str(data))
tiedosto.close()
