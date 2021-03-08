strawberries_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price * 0.5
orange_price = raspberries_price * 0.6
banana_price = raspberries_price * 0.2

money = (strawberries_kg * strawberries_price) + (banana_kg * banana_price) + (orange_kg * orange_price) + (raspberries_kg * raspberries_price)

print (str(money))