n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if 1 <= num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

per1 = p1 / n * 100
print(f"{per1:.2f}%")
per2 = p2 / n * 100
print(f"{per2:.2f}%")
per3 = p3 / n * 100
print(f"{per3:.2f}%")
per4 = p4 / n * 100
print(f"{per4:.2f}%")
per5 = p5 / n * 100
print(f"{per5:.2f}%")