projection = str(input())
row = int(input())
column = int(input())

profit = 0

if projection == "Premiere":
    profit = (row * column) * 12

elif projection == "Normal":
    profit = (row * column) * 7.5

elif projection == "Discount":
    profit = (row * column) * 5

print(f"{profit:.2f} leva")