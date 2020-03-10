import Adafruit_DHT
import datetime
from datetime import date
import time
from datetime import date
import os

today = date.today()
time2 = datetime.datetime.now()
record_secs = 28800 # seconds to record (default for 12 hours is 43200 seconds)
dir = '/home/pi/Desktop/FrogFiles/Audio/' + str(today)
CHECK_FOLDER = os.path.isdir(dir)
if not CHECK_FOLDER:
    os.mkdir(dir)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 6
file = open(dir + '/' + str(today) + '.txt', 'w')
#Create text format
file.write('Time\t  Temperature\tHumidity\n')

end = time.time() + record_secs # Default is 43200 sec which is 8 hours

try:
    while time.time() < end:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            currentTimeLong = datetime.datetime.now()
            currentTime = currentTimeLong.strftime("%H:%M:%S")
            file.write(currentTime + "  " + str(temperature) + " \t\t" + str(humidity) + "\n")
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
 
except KeyboardInterrupt:
        print("File Stopped")
        
file.close()
    