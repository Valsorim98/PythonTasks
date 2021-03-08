hour = int(input())
min = int(input())

min += 15

if min >= 60:
    min -= 60
    hour += 1

if hour >= 24:
    hour -= 24

if min < 10:
    print(str(hour) + ":0" + str(min))

elif min >= 10:
    print(str(hour) + ":" + str(min))