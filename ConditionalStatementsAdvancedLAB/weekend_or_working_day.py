DAY = str(input("Please type a day of the week: "))

if DAY in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Working day")
elif DAY in ("Saturday", "Sunday"):
    print("Weekend")
else:
    print("no " + str(DAY) + " found")
    