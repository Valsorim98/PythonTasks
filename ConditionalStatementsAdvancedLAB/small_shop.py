PRODUCT = str(input())
CITY = str(input())
QUANTITY = float(input())

PRICE = 0

if CITY == "Sofia":
    if PRODUCT == "coffee":
        PRICE = QUANTITY * 0.5
        print(PRICE)
    elif PRODUCT == "water":
        PRICE = QUANTITY * 0.8
        print(PRICE)
    elif PRODUCT == "beer":
        PRICE = QUANTITY * 1.2
        print(PRICE)
    elif PRODUCT == "sweets":
        PRICE = QUANTITY * 1.45
        print(PRICE)
    elif PRODUCT == "peanuts":
        PRICE = QUANTITY * 1.6
        print(PRICE)

if CITY == "Plovdiv":
    if PRODUCT == "coffee":
        PRICE = QUANTITY * 0.4
        print(PRICE)
    elif PRODUCT == "water":
        PRICE = QUANTITY * 0.7
        print(PRICE)
    elif PRODUCT == "beer":
        PRICE = QUANTITY * 1.15
        print(PRICE)
    elif PRODUCT == "sweets":
        PRICE = QUANTITY * 1.3
        print(PRICE)
    elif PRODUCT == "peanuts":
        PRICE = QUANTITY * 1.5
        print(PRICE)

if CITY == "Varna":
    if PRODUCT == "coffee":
        PRICE = QUANTITY * 0.45
        print(PRICE)
    elif PRODUCT == "water":
        PRICE = QUANTITY * 0.7
        print(PRICE)
    elif PRODUCT == "beer":
        PRICE = QUANTITY * 1.1
        print(PRICE)
    elif PRODUCT == "sweets":
        PRICE = QUANTITY * 1.35
        print(PRICE)
    elif PRODUCT == "peanuts":
        PRICE = QUANTITY * 1.55
        print(PRICE)
        