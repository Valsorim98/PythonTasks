n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

per1 = p1 / n * 100
print(f"{per1:.2f}%")
per2 = p2 / n * 100
print(f"{per2:.2f}%")
per3 = p3 / n * 100
print(f"{per3:.2f}%")