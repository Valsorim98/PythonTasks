PRODUCT = str(input())

if PRODUCT in ("banana", "apple", "kiwi", "cherry", "lemon", "grapes"):
    print("fruit")
elif PRODUCT in ("tomato", "cucumber", "pepper", "carrot"):
    print("vegetable")
else:
    print("unknown")
