import math

income = float(input())
average_grade = float(input())
min_wage = float(input())

social_scholarship = min_wage * 0.35
scholarship = average_grade * 25
wss = 0
ws = 0

if average_grade < 5.5 and income > min_wage or average_grade < 4.5:
    print("You cannot get a scholarship!")
    exit()

if income < min_wage and 4.5 <= average_grade:
    wss = 1
else:
    wss = 0

if average_grade >= 5.5:
    ws = 1
else:
    ws = 0

if wss == 1 and ws == 1:
    if social_scholarship > scholarship:
        print("You get a Social scholarship " + str(math.floor(social_scholarship)) + " BGN")
    if scholarship >= social_scholarship:
        print("You get a scholarship for excellent results " + str(math.floor(scholarship)) + " BGN")