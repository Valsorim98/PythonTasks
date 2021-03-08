days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cake_price = 45
waffles_price = 5.8
pancakes_price = 3.2

money_day = ((cakes * 45) + (waffles * 5.8) + (pancakes * 3.2)) * bakers
funds_gathered = money_day * days
taxes = funds_gathered / 8
total_sum = funds_gathered - taxes

print (str(total_sum))