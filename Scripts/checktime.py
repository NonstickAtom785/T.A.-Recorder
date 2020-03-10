import datetime
import os

now = datetime.datetime.now()

if now.hour > 20 or now.hour < 8:
    os.system('python temp2.py & python audio.py &')