PRODUCT = str(input("Please type a fruit or vegetable: "))

fruits = ("banana", "apple", "kiwi", "cherry", "lemon", "grapes")
vegetables = ("tomato", "cucumber", "pepper", "carrot")

def is_fruit(PRODUCT):
    """Shows if the product is a fruit.

    Args:
        PRODUCT (str): Product name.

    Returns:
        bool: Returns True if its a fruit, else False.
    """    
    return PRODUCT in fruits

def is_vegetable(PRODUCT):
    """Shows if the product is a vegetable.

    Args:
        PRODUCT (str): Product name.

    Returns:
        bool: Returns True if the product is a vegetable, else False.
    """    
    return PRODUCT in vegetables

if is_fruit(PRODUCT):
    print("fruit")
elif is_vegetable(PRODUCT):
    print("vegetable")
else:
    print(f"no {PRODUCT} found!")
