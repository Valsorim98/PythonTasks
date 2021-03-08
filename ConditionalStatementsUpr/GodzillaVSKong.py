budget = float(input())
statists = int(input())
clothes = float(input())

if 1 > budget or budget > 1000000:
    print("Wrong")
    exit()

elif 1 > statists or statists > 500:
    print("Wrong")
    exit()

elif 1 > clothes or clothes > 1000:
    print("Wrong")
    exit()

decor = budget * 0.1

if statists > 150:
    clothes *= 0.9

elif statists < 150:
    clothes = clothes

clothes = statists * clothes

expenses = decor + clothes
insufficient = abs(budget - expenses)
total = budget - expenses

if expenses > budget:
    print("Not enough money!")
    print("Wingard needs " + f"{insufficient:.2f}" + " leva more.")

elif expenses <= budget:
    print("Action!")
    print("Wingard starts filming with " + f"{total:.2f}" + " leva left.")