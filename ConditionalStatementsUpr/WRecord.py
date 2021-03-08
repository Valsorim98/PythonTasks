import math

WRecord = float(input())
distance = float(input())
time_m = float(input())

Ivan_time = 0
stream = math.floor(distance / 15)
Ivan_time += distance * time_m
Ivan_time += stream * 12.5
Ivan_time = round(Ivan_time, 2)

final = abs(WRecord - Ivan_time)

if Ivan_time < WRecord:
    print("Yes, he succeeded! The new world record is " + f"{Ivan_time:.2f}" + " seconds.")

elif Ivan_time > WRecord:
    print("No, he failed! He was " + f"{final:.2f}" + " seconds slower.")