degrees = int(input())
day_time = str(input())

Outfit = ''
Shoes = ''

if 10 <= degrees <= 18:
    if day_time == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    if day_time == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif 18 < degrees <= 24:
    if day_time == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if day_time == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif degrees >= 25:
    if day_time == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    if day_time == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print("It's " + str(degrees) + " degrees, get your " + str(Outfit) + " and " + str(Shoes) + ".")