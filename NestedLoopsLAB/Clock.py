h = 0
m = 0

for h in range(24):
    for m in range(60):
        if m == 60:
            h += 1
            m = 0
        print(f"{h}:{m}")
    m += 1