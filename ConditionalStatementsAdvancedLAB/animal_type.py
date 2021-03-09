ANIMAL = str(input())

if ANIMAL == "dog":
    print("mammal")
elif ANIMAL in ("crocodile", "tortoise", "snake"):
    print("reptile")
else:
    print("unknown")
