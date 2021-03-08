fruit = str(input())
day = str(input())
quantity = float(input())

price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = quantity * 2.5
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "apple":
        price = quantity * 1.2
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "orange":
        price = quantity * 0.85
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "grapefruit":
        price = quantity * 1.45
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "kiwi":
        price = quantity * 2.7
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "pineapple":
        price = quantity * 5.5
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "grapes":
        price = quantity * 3.85
        print(f"{round(price, 2):.2f}")
        exit()
    else:
        print("error")

if day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.7
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "apple":
        price = quantity * 1.25
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "orange":
        price = quantity * 0.90
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "grapefruit":
        price = quantity * 1.60
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "kiwi":
        price = quantity * 3.0
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "pineapple":
        price = quantity * 5.6
        print(f"{round(price, 2):.2f}")
        exit()
    elif fruit == "grapes":
        price = quantity * 4.2
        print(f"{round(price, 2):.2f}")
        exit()
    else:
        print("error")

if day != "Monday":
    print("error")
    exit()
elif day != "Tuesday":
    print("error")
    exit()
elif day != "Wednesday":
    print("error")
    exit()
elif day != "Thursday":
    print("error")
    exit()
elif day != "Friday":
    print("error")
    exit()
elif day != "Saturday":
    print("error")
    exit()
elif day != "Sunday":
    print("error")
    exit()
else:
    exit()