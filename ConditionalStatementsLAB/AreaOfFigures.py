import math

type = input()

if type == 'square':
    a = float(input())
    s = math.pow(a, 2)
    print (f"{s:.3f}")
elif type == 'rectangle':
    b = float(input())
    c = float(input())
    s = b * c
    print (f"{s:.3f}")
elif type == 'circle':
    r = float(input())
    s = math.pi * math.pow(r, 2)
    print (f"{s:.3f}")
elif type == 'triangle':
    d = float(input())
    h = float(input())
    s = d * (0.5 * h)
    print (f"{s:.3f}")

