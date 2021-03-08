start = int(input())

bonus = 0

if start <= 100:
    bonus += 5
elif 100 < start < 1000:
    bonus = bonus + (start * 0.2)
elif start > 1000:
    bonus = bonus + (start * 0.1)

if start % 2 == 0:
    bonus += 1

if start % 10 == 5:
    bonus += 2

total_points = start + bonus

print(bonus)
print(total_points)