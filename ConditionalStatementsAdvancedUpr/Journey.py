budget = float(input())
season = str(input())

spent = 0

if budget <= 100:
    if season == "summer":
        spent = budget * 0.3
    elif season == "winter":
        spent = budget * 0.7
    print("Somewhere in Bulgaria")

if 100 < budget <= 1000:
    if season == "summer":
        spent = budget * 0.4
    elif season == "winter":
        spent = budget * 0.8
    print("Somewhere in Balkans")

if budget > 1000:
    spent = budget * 0.9
    print("Somewhere in Europe")

if season == "summer" and budget < 1000:
    print(f"Camp - {spent:.2f}")
elif season == "winter" or budget > 1000:
    print(f"Hotel - {spent:.2f}")