length = int(input())
width = int(input())
height = int(input())
occupied_cap = float(input())

capacity = length * width * height
water_lit = capacity * 0.001
occupied = occupied_cap * 0.01

total_lit = water_lit * (1 - occupied)
print (str(total_lit))