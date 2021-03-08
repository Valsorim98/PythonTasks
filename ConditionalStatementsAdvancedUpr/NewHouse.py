type = str(input())
pieces = int(input())
budget = int(input())

price = 0

if type == "Roses":
    price = pieces * 5
    if pieces > 80:
        price *= 0.9
elif type == "Dahlias":
    price = pieces * 3.8
    if pieces > 90:
        price *= 0.85
elif type == "Tulips":
    price = pieces * 2.8
    if pieces > 80:
        price *= 0.85
elif type == "Narcissus":
    price = pieces * 3
    if pieces < 120:
        price *= 1.15
elif type == "Gladiolus":
    price = pieces * 2.5
    if pieces < 80:
        price *= 1.2

total = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {pieces} {type} and {total:.2f} leva left.")
elif budget < price:
    print(f"Not enough money, you need {total:.2f} leva more.")