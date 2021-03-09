HOUR = int(input())
DAY = str(input())

if 10 <= HOUR <= 18:
    if DAY in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
        print("open")
    else:
        print("closed")
else:
    print("closed")
