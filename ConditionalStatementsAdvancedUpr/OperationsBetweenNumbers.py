N1 = int(input())
N2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result:} - even")
    elif result % 2 != 0:
        print(f"{result:.2f} - odd")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    elif result % 2 != 0:
        print(f"{N1} {operator} {N2} = {result} - odd")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    elif result % 2 != 0:
        print(f"{N1} {operator} {N2} = {result} - odd")
elif operator == "/" and N2 != 0:
    result = N1 / N2
    print(f"{N1} {operator} {N2} = {result:.2f}")
elif operator == "%" and N2 != 0:
    result = N1 % N2
    print(f"{N1} {operator} {N2} = {result}")
elif operator == "/" or operator == "%" and N2 == 0:
    print(f"Cannot divide {N1} by zero")