import math

numbers = int(input())

max_num = 0
min_num = math.inf

for i in range(0, numbers):
    num = int(input())
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print("Max number: " + str(max_num))
print("Min number: " + str(min_num))