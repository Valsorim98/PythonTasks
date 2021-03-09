ANIMAL = str(input("Please type a life form: "))

reptiles = ("crocodile", "tortoise", "snake")
mammals = ("dog", "cat")

def is_reptile(ANIMAL):

    return ANIMAL in reptiles

def is_mammal(ANIMAL):

    return ANIMAL in mammals

if is_reptile(ANIMAL):
    print("reptile")
elif is_mammal(ANIMAL):
    print("mammal")
else:
    print("no " + str(ANIMAL) + " found")
