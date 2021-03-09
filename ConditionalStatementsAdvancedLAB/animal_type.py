ANIMAL = str(input("Please type a life form: "))

reptiles = ("crocodile", "tortoise", "snake")
mammals = ("dog", "cat")

def is_reptile(ANIMAL):
    """ Shows the animals which are reptile.

    Args:
        ANIMAL (str): Animal name.

    Returns:
        bool: Returns True if its a reptile, else False.
    """    
    return ANIMAL in reptiles

def is_mammal(ANIMAL):
    """Show the animals which are mammal.

    Args:
        ANIMAL (str): Animal name.

    Returns:
        bool: Returns True if its a mammal, else False.
    """
    return ANIMAL in mammals

if is_reptile(ANIMAL):
    print("reptile")
elif is_mammal(ANIMAL):
    print("mammal")
else:
    print(f"no {ANIMAL} found!")

