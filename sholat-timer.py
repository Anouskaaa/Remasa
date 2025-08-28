from time import sleep
from datetime import datetime as dt
from datetime import timedelta
import pytz
import salat
import os
# import threading
import geocoder


tz = pytz.timezone("Asia/Jakarta")
pt = salat.PrayerTimes(salat.CalculationMethod.MWL, salat.AsrMethod.STANDARD)
# long = 107.61912
# lat = -6.91746
g = geocoder.ip('me')
shalat_lanjutan = None

print("Process ID : ", os.getpid())
next_salat = None
rm_microsec = None


current_day = dt.now().date()

print(dt.now(tz))


while True:
    now = dt.now(tz)
    prayer_times = pt.calc_times(current_day, tz, g.lng, g.lat)
    for name, time in prayer_times.items():
        readable_time = time.strftime("%m/%d/%Y, %I:%M:%S %p %Z")
        if name == "fajr":
            name == "shubuh"
        if time > now:
            shalat_lanjutan = (name, time)
            break

    if shalat_lanjutan:
        count_time = shalat_lanjutan[1] - now
        rm_microsec = str(count_time).split(".")[0]
        next_salat = shalat_lanjutan[0]
        print(f"\rShalat berikut nya {next_salat} : {rm_microsec}", end="")
        sleep(1)

    elif not shalat_lanjutan:
        besok = current_day + timedelta(days=1)
        prayer_times = pt.calc_times(besok, tz, long, lat)
        current_day = besok
        continue









