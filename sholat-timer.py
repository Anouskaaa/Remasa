# from PyQt6.QtWidgets import QApplication, QtWidgets
from time import sleep
from datetime import datetime as dt 
from datetime import timedelta
import pytz
import salat

pt = salat.PrayerTimes(salat.CalculationMethod.MWL, salat.AsrMethod.STANDARD)
tz = pytz.timezone("Asia/Jakarta")
long = 107.61912
lat = -6.91746

current_day = dt.now().date()
prayer_times = pt.calc_times(current_day, tz, long, lat)
while True:
    now = dt.now(tz)
    shalat_lanjutan = None
    for name, time in prayer_times.items():
        readable_time = time.strftime("%m/%d/%Y, %I:%M:%S %p %Z")
        # print(f"Shalat : {name}, Waktu : {readable_time}\n")
        if time > now:
            shalat_lanjutan = (name, time)
            break

    if shalat_lanjutan:
        print(shalat_lanjutan[1], " : ", now)
        count_time = shalat_lanjutan[1] - now
        rm_microsec = str(count_time).split(".")[0] # split after titik jadi 2 array ambil array pertama [0]
        print(f"Waktu shalat berikut nya : {rm_microsec}")
            
    elif not shalat_lanjutan:
        besok = current_day + timedelta(days=1)
        prayer_times = pt.calc_times(besok, tz, long, lat)
        current_day = besok
        print("test")
        continue
        # else:
        #     print("Sudah 5 Waktu hari ini.")
    sleep(1)
