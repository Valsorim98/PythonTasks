city = str(input())
sales = float(input())

com = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        com = sales * 0.05
        print(f"{com:.2f}")
        exit()
    elif 500 < sales <= 1000:
        com = sales * 0.07
        print(f"{com:.2f}")
        exit()
    elif 1000 < sales <= 10000:
        com = sales * 0.08
        print(f"{com:.2f}")
        exit()
    elif sales > 10000:
        com = sales * 0.12
        print(f"{com:.2f}")
        exit()
    elif sales < 0:
        print("error")
        exit()

if city == "Varna":
    if 0 <= sales <= 500:
        com = sales * 0.045
        print(f"{com:.2f}")
        exit()
    elif 500 < sales <= 1000:
        com = sales * 0.075
        print(f"{com:.2f}")
        exit()
    elif 1000 < sales <= 10000:
        com = sales * 0.1
        print(f"{com:.2f}")
        exit()
    elif sales > 10000:
        com = sales * 0.13
        print(f"{com:.2f}")
        exit()
    elif sales < 0:
        print("error")

if city == "Plovdiv":
    if 0 <= sales <= 500:
        com = sales * 0.055
        print(f"{com:.2f}")
        exit()
    elif 500 < sales <= 1000:
        com = sales * 0.08
        print(f"{com:.2f}")
        exit()
    elif 1000 < sales <= 10000:
        com = sales * 0.12
        print(f"{com:.2f}")
        exit()
    elif sales > 10000:
        com = sales * 0.145
        print(f"{com:.2f}")
        exit()
    elif sales < 0:
        print("error")

elif city != "Sofia" or city != "Varna" or city != "Plovdiv":
    print("error")