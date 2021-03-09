import sys

FRUIT = str(input())
DAY = str(input())
QUANTITY = float(input())

PRICE = 0

if DAY in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if FRUIT == "banana":
        PRICE = QUANTITY * 2.5
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "apple":
        PRICE = QUANTITY * 1.2
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "orange":
        PRICE = QUANTITY * 0.85
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "grapefruit":
        PRICE = QUANTITY * 1.45
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "kiwi":
        PRICE = QUANTITY * 2.7
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "pineapple":
        PRICE = QUANTITY * 5.5
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "grapes":
        PRICE = QUANTITY * 3.85
        print(f"{round(PRICE, 2):.2f}")

    else:
        print("error")

if DAY in ("Saturday", "Sunday"):
    if FRUIT == "banana":
        PRICE = QUANTITY * 2.7
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "apple":
        PRICE = QUANTITY * 1.25
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "orange":
        PRICE = QUANTITY * 0.90
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "grapefruit":
        PRICE = QUANTITY * 1.60
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "kiwi":
        PRICE = QUANTITY * 3.0
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "pineapple":
        PRICE = QUANTITY * 5.6
        print(f"{round(PRICE, 2):.2f}")

    elif FRUIT == "grapes":
        PRICE = QUANTITY * 4.2
        print(f"{round(PRICE, 2):.2f}")

    else:
        print("error")

if DAY != "Monday":
    print("error")

elif DAY != "Tuesday":
    print("error")

elif DAY != "Wednesday":
    print("error")

elif DAY != "Thursday":
    print("error")

elif DAY != "Friday":
    print("error")

elif DAY != "Saturday":
    print("error")

elif DAY != "Sunday":
    print("error")

else:
    sys.exit()
