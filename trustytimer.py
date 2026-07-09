import time

mytime = input("set a timer for? (HH:MM:SS) ")

hours = int(mytime[0:2])
minutes = int(mytime[3:5])
seconds = int(mytime[6:8])

totalseconds = (hours*3600) + (minutes*60) + (seconds)

for x in range(totalseconds, 0, -1):
    h = x // 3600
    m = (x % 3600) // 60
    s = x % 60

    print(f"{h:02d}:{m:02d}:{s:02d}")
    time.sleep(1)

print("TIME'S UPPP")
