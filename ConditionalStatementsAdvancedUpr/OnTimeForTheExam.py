import math

start_hour = int(input())
start_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

start_time = start_hour * 60 + start_min
arrive_time = arrive_hour * 60 + arrive_min
diff = arrive_time - start_time

hh = abs(diff) // 60
mm = abs(diff) % 60

if diff >= 1:
    print("Late")
    if diff <= 59:
        print(f"{mm} minutes after the start")
    elif diff >= 60:
        print(f"{hh}:{mm:02d} hours after the start")
elif -30 <= diff <= 0:
    print("On time")
    if -30 <= diff < 0:
        print(f"{mm} minutes before the start")
elif diff < -30:
    print("Early")
    if -59 <= diff <= -1:
        print(str(mm) + " minutes before the start")
    elif diff == -60:
        print(f"{hh}:{mm:02d} hours before the start")
    elif diff < -60:
        print(f"{hh}:{mm:02d} hours before the start")