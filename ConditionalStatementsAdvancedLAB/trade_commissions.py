CITY = str(input())
SALES = float(input())

COM = 0

if CITY == "Sofia":
    if 0 <= SALES <= 500:
        COM = SALES * 0.05
        print(f"{COM:.2f}")

    elif 500 < SALES <= 1000:
        COM = SALES * 0.07
        print(f"{COM:.2f}")

    elif 1000 < SALES <= 10000:
        COM = SALES * 0.08
        print(f"{COM:.2f}")

    elif SALES > 10000:
        COM = SALES * 0.12
        print(f"{COM:.2f}")

    elif SALES < 0:
        print("error")


if CITY == "Varna":
    if 0 <= SALES <= 500:
        COM = SALES * 0.045
        print(f"{COM:.2f}")

    elif 500 < SALES <= 1000:
        COM = SALES * 0.075
        print(f"{COM:.2f}")

    elif 1000 < SALES <= 10000:
        COM = SALES * 0.1
        print(f"{COM:.2f}")

    elif SALES > 10000:
        COM = SALES * 0.13
        print(f"{COM:.2f}")

    elif SALES < 0:
        print("error")

if CITY == "Plovdiv":
    if 0 <= SALES <= 500:
        COM = SALES * 0.055
        print(f"{COM:.2f}")

    elif 500 < SALES <= 1000:
        COM = SALES * 0.08
        print(f"{COM:.2f}")

    elif 1000 < SALES <= 10000:
        COM = SALES * 0.12
        print(f"{COM:.2f}")

    elif SALES > 10000:
        COM = SALES * 0.145
        print(f"{COM:.2f}")

    elif SALES < 0:
        print("error")

elif CITY != "Sofia" or CITY != "Varna" or CITY != "Plovdiv":
    print("error")
