AGE = float(input())
GENDER = str(input())

if GENDER == "m" and AGE >= 16:
    print("Mr.")

if GENDER == "m" and AGE < 16:
    print("Master")

if GENDER == "f" and AGE >= 16:
    print("Ms.")

if GENDER == "f" and AGE < 16:
    print("Miss")
    