from time import sleep
from datetime import datetime as dt 
from datetime import timedelta
import pytz
import salat
import threading
import os
import signal


print(f"Process ID : ", os.getpid())
next_salat = None
rm_microsec = None




current_day = dt.now().date()


try:
    while True:

        pt = salat.PrayerTimes(salat.CalculationMethod.MWL, salat.AsrMethod.STANDARD)
        tz = pytz.timezone("Asia/Jakarta")
        long = 107.61912
        lat = -6.91746
        now = dt.now(tz)
        shalat_lanjutan = None
        name = None

        prayer_times = pt.calc_times(current_day, tz, long, lat)


        

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
            
            print(f"Shalat berikut nya {next_salat} : {rm_microsec}")
            
        elif not shalat_lanjutan:
            besok = current_day + timedelta(days=1)
            prayer_times = pt.calc_times(besok, tz, long, lat)
            current_day = besok
            print("test")
            continue
        sleep(1)
except KeyboardInterrupt:
    print("Process ended by user")








