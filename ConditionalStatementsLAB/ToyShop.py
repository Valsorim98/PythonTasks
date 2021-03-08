excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_cost = 2.6
doll_cost = 3
bear_cost = 4.1
minion_cost = 8.2
truck_cost = 2

pieces = puzzles + dolls + bears + minions + trucks
order = (2.6 * puzzles + 3 * dolls + 4.1 * bears + 8.2 * minions + 2 * trucks)

if pieces >= 50:
    order *= 0.75
else:
    order = order

order *= 0.9

if order >= excursion:
    order -= excursion
    print (f"Yes! {order:.2f} lv left.")
else:
    order = abs(order - excursion)
    print (f"Not enough money! {order:.2f} lv needed.")