age = float(input())
gender = str(input())

if gender == "m" and age >= 16:
    print("Mr.")

if gender == "m" and age < 16:
    print("Master")

if gender == "f" and age >= 16:
    print("Ms.")

if gender == "f" and age < 16:
    print("Miss")