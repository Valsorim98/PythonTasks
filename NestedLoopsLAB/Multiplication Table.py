x = 1
y = 0

for i in range(100):
    y += 1
    if y == 11:
        x += 1
        y = 1
    res = x * y
    print(f"{x} * {y} = {res}")