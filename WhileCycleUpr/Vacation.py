excursion_price = float(input())
available_money = float(input())

days = 0
spend_days = 0

while available_money < excursion_price:
    action = str(input())
    money = float(input())
    days += 1
    if action == "save":
        available_money += money
        spend_days = 0
        if available_money >= excursion_price:
            print(f"You saved the money for {days} days.")
    elif action == "spend":
        available_money -= money
        spend_days += 1
        if available_money < 0:
            available_money = 0
        if spend_days == 5:
            print(f"You can't save the money.")
            print(days)